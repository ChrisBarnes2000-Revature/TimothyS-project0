from calendar import week
from calendar import timegm
import datetime
from operator import itemgetter

# dicts holding medications and prescribed date & time (for now until creating separate module)
userMedsMonday = {0800: 'Pill A', 2000: 'Pill B', 0800: 'Pill C', 2000: 'Pill D'}
userMedsTuesday = {0800: 'Pill E', 1800: 'Pill D'}
userMedsWednesday = {0800: 'Pill A', 2000: 'Pill B', 0800: 'Pill C', 2000: 'Pill D'}
userMedsThursday = {0800: 'Pill E', 1800: 'Pill D'}
userMedsFriday = {0800: 'Pill A', 2000: 'Pill B', 0800: 'Pill C', 2000: 'Pill D'}

# Medication reminder program by Timothy S.
# Purpose is to remind user of what medications to take at specific time on the day of the week


print('Hello and welcome to your medication reminder!')

# Input day of the week and current time
current_day = str(input('Please type the current day of the week: '))
current_time = input(
    'Please enter the current time in 24-hour format: ')
print('Now searching for prescribed medications on ' +
      current_day + ' at ' + current_time)

# Searching for medications to be taken at inputted day and time
if current_day == 'Monday':
    if current_time >= 0800:
        print(userMedsMonday.get(0800))
    elif current_time >= 2000:
        print(userMedsMonday.get(2000))
