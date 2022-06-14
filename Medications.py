from calendar import week
from calendar import timegm
import datetime
from operator import itemgetter


days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

# Data Structures containing prescribed medications and their day and time to be taken (Time to take medication: Medications prescribed)
monday_meds = {'800': 'Pill A, Pill B, Pill C', '1800': 'Pill A, Pill D'}
tuesday_meds = {'800': 'Pill E, PIll F', '1800': 'Pill E'}
wednesday_meds = {'800': 'Pill A, Pill B, Pill C', '1800': 'Pill A, Pill D'}
thursday_meds = {'800': 'Pill E, Pill F', '1800': 'Pill E'}
friday_meds = {'800': 'Pill A, Pill B, Pill C', '1800': 'Pill A, Pill D'}
saturday_meds = {'800': 'Pill G', '2100': 'Pill H'}
sunday_meds = {'800': 'Pill G', '2100': 'Pill H'}


# Function that returns the prescribed medications on the given day and time
def get_meds(day, time):
    for x in days_of_the_week:
        if day == x:
            if x == 'Monday':
                return monday_meds.get(time)
            elif x == 'Tuesday':
                return tuesday_meds.get(time)
            elif x == 'Wednesday':
                return wednesday_meds.get(time)
            elif x == 'Thursday':
                return thursday_meds.get(time)
            elif x == 'Friday':
                return friday_meds.get(time)
            elif x == 'Saturday':
                return saturday_meds.get(time)
            elif x == 'Sunday':
                return sunday_meds.get(time)
