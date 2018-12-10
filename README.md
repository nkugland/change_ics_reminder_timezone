# change_ics_reminder_timezone
A script to change the timezone of the reminders in a .ics file. Useful when you have Mac or iOS reminders set up at certain times and then you travel into a new timezone.

# Usage

## Workflow
1. On a Mac, open Reminders.app
2. Select reminders that need their timezones converted
3. Drag to the Finder to create a .ics file
4. Run the .ics file through this script
5. Update the VTIMEZONE block manually (create a single reminder in the new time zone, drag to the Finder, copy & paste the VTIMEZONE block into the 

## Script usage
Given a file `reminders.ics` with reminders created in US Pacific time:

`python convert_ics_timezone.py --file reminders.ics --new_timezone America/New_York --old_timezone America/Los_Angeles`

...generates a file `tz converted reminders.ics` with event-level timestamps converted to US Eastern time.