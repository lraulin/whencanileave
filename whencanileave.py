#!/bin/python3

from pathlib import Path
from inspect import getframeinfo, currentframe
from datetime import date, time, datetime, timedelta
from dateutil.tz import tzlocal
from pytz import timezone
from sys import stdin
from dateparser import parse

earliest = parse(f"{date.today().strftime(r'%Y-%m-%d')} 07:00:00 -0500")
today = date.today().strftime(r'%Y-%m-%d')

# Ensure filepath for data files is in module directory regardless of cwd.
FILENAME = getframeinfo(currentframe()).filename
PARENT = Path(FILENAME).resolve().parent
FILE = PARENT / 'today.txt'
LOG = PARENT / 'timesheet.csv'
TIMEZONE = "-0500"

logs = []
arrival_time = None

for line in stdin:
    log = [parse(line[:25]), line[26:46].strip(), line[48:]]
    if log[0] > earliest:
        arrival_time = log[0]
        break

if arrival_time == None:
    print("Error: Couldn't find arrival time")
    exit()

quitting_time = arrival_time + timedelta(hours=8)
leave_time_str = quitting_time.strftime('%I:%M %p')
print(f"You can leave at {leave_time_str}")

with open(LOG, 'r') as f:
    data = f.readlines()
    lastline = data[-1]
    lastdate = lastline.split(',')[0]
    if today != lastdate:
        with open(LOG, 'a+') as f:
            f.write(
                f'\n{today},{leave_time_str}')
