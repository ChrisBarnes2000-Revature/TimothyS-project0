# Medication reminder program by Timothy S.
# Purpose is to remind user of what medications to take at specific time on the day of the week

import datetime
from operator import itemgetter

import Medications
from Clients.TimothyMedList import MedList
from Utils import Utils

if __name__ == '__main__':
    # Start of program
    print('Hello and welcome to your medication reminder!')

    # Input day of the week and current time
    current_day = Utils["get_current_day"]()
    current_time = Utils["get_current_time"]()

    """ Because medications can still be taken "2 hours" before or after the inputted time,
        * we want it to display a dict containing the range of time "2 hours" before through "2 hours" after
        * we want it to display the exact time as well
    """

    # Search for medications to be taken at inputted day and time
    current_meds = Medications.get_current_meds(MedList, current_day, current_time)
    # Get window for "acceptable" medication
    meds_window = Medications.get_meds_window(MedList, current_day, current_time, offset="0200")

    print(current_meds)
    print(meds_window)
