#!/usr/bin/env python
"""
Example usage: python convert_ics_timezone.py --file reminders.ics --new_timezone America/New_York --old_timezone America/Los_Angeles

Outputs file `tz converted reminders.ics`

Note that the VTIMEZONE block at the top is unmodified so it's necessary to manually copy a new 
VTIMEZONE after running this script. You can make a single event in the new timezone to 
generate a new VTIMEZONE block.

TODO: rewrite UIDs? So events don't overwrite.

Simple script that updates Mac & iOS reminders to a new timezone. 
Requires icalendar package (which pulls in pytz as a dependency).

Adapted from https://gist.github.com/deybhayden/1980583 by @beardedprojamz (Ben Hayden)
"""
import argparse
import sys

import pytz
from icalendar import Calendar
from pytz import timezone, UTC
from datetime import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script to convert an ics calendar & events to the passed timezone.')
    parser.add_argument("--file", "-f", dest='file', help='The ics file to parse and update.', required=True)
    parser.add_argument("--new_timezone", "-tn", dest='new_timezone', help='The timezone used to update the ics file', required=True)
    parser.add_argument("--old_timezone", "-to", dest='old_timezone', help='', required=True)
    args = parser.parse_args()

    cal = Calendar.from_ical(open(args.file, 'rb').read())

    try:
        newtz = timezone(args.new_timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        sys.exit('Invalid timezone; unable to update ics file.')

    try:
        oldtz = timezone(args.old_timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        sys.exit('Invalid timezone; unable to update ics file.')


    for component in cal.walk():
        if component.name == 'VTODO':
            dtstart = component.get('DTSTART')
            if dtstart is not None:
                dtstart.params['TZID'] = str(newtz)

            due = component.get('DUE')
            if due is not None:
                due.params['TZID'] = str(newtz)

        if component.name == 'VALARM':
            dttrigger = component.get('TRIGGER')

            step1 = newtz.localize(dttrigger.dt.replace(tzinfo=None))
            step2 = step1.astimezone(oldtz).replace(tzinfo=UTC)

            dttrigger.dt = step2

    open('tz converted ' + args.file, 'wb').write(cal.to_ical())