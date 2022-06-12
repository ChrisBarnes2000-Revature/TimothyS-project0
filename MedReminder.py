from calendar import week
from calendar import timegm
import datetime

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
