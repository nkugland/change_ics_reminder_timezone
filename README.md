# change_ics_reminder_timezone
A script to change the timezone of the reminders in a .ics file. Useful when you have Mac or iOS reminders set up at certain times and then you travel into a new timezone.

# Usage

## Script usage
Given a file `Reminders.ics` with reminders created in US Pacific time:

`python convert_ics_timezone.py --file Reminders.ics --new_timezone America/New_York --old_timezone America/Los_Angeles`

...generates a file `tz converted Reminders.ics` with event-level timestamps converted to US Eastern time.

## Workflow
1. On a Mac, open Reminders.app
2. Select reminders that need their timezones converted
3. Drag to the Finder to create a `Reminders.ics` file
4. Run the `Reminders.ics` file through this script (see above)
5. Update the VTIMEZONE block manually: create a single reminder in the new time zone, drag to the Finder, copy & paste the VTIMEZONE block into the converted file
6. Drag `tz converted Reminders.ics` back into Reminders.app. The converted events in the new time zone will replace their counterparts in the old time zone.
