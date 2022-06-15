import datetime
from operator import itemgetter


days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

# Data Structures containing prescribed medications and their day and time to be taken (Time to take medication: Medications prescribed)
monday_meds = {'0800': 'Pill A, Pill B, Multi-Vitamins',
               '1100': 'Pill C', '1800': 'Pill A, Pill D'}
tuesday_meds = {'0800': 'Pill E, PIll F, Multi-Vitamins',
                '1100': 'Pill C', '1800': 'Pill E'}
wednesday_meds = {'0800': 'Pill A, Pill B, Multi-Vitamins',
                  '1100': 'Pill C', '1800': 'Pill A, Pill D'}
thursday_meds = {'0800': 'Pill E, Pill F, Multi-Vitamins',
                 '1100': 'Pill C', '1800': 'Pill E'}
friday_meds = {'0800': 'Pill A, Pill B, Multi-Vitamins',
               '1100': 'Pill C', '1800': 'Pill A, Pill D'}
saturday_meds = {'0900': 'Pill G, Multi-Vitamins',
                 '1100': 'Pill C', '2100': 'Pill H'}
sunday_meds = {'0900': 'Pill G, Multi-Vitamins',
               '1100': 'Pill C', '2100': 'Pill H'}


# Function that returns the prescribed medications on the given day and time
def get_meds(day, time):

    # Returning prescribed medications to take on given time (fitting in time range of two hours before and after) and day
    for x in days_of_the_week:
        if day == x:
            if x == 'Monday':
                return [m for t, m in monday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
            elif x == 'Tuesday':
                return [m for t, m in tuesday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
            elif x == 'Wednesday':
                return [m for t, m in wednesday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
            elif x == 'Thursday':
                return [m for t, m in thursday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
            elif x == 'Friday':
                return [m for t, m in friday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
            elif x == 'Saturday':
                return [m for t, m in saturday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
            elif x == 'Sunday':
                return [m for t, m in sunday_meds.items() if (int(t) - 200) <= int(time) <= (int(t) + 200)]
