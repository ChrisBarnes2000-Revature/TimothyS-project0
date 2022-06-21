# Medication reminder program by Timothy S.
# Purpose is to remind user of what medications to take at specific time on the day of the week
import json

import Medications
from Clients.Timothy import Timothy_MedList as MedList
from Utils import Utils

if __name__ == '__main__':
    """ Because medications can still be taken "2 hours" before or after the inputted time,
        * we want it to display a dict containing the range of time "2 hours" before through "2 hours" after
        * we want it to display the exact time as well
    """

    # Start of program
    print('Hello and welcome to your medication reminder!')

    # Input day of the week and current time
    given_day = "monday"  # Utils["get_current_day"]()
    given_time = "2130"  # Utils["get_current_time"]()
    offset = ["0200", "00"]
    current = [given_day, str(given_time)[:2]+"00", str(given_time)[2:]]
    day, hour, minute = current

    # Search for "acceptable" medications to be taken at inputted day and time
    meds_within_the_hour = Medications.get_current_meds(MedList, day, hour)
    meds_at_specific_min = Medications.get_current_meds(MedList, day, hour, minute)

    meds_before = Medications.get_current_meds(MedList, day, hour, minute)
    meds_current = Medications.get_current_meds(MedList, day, hour, minute)
    meds_after = Medications.get_current_meds(MedList, day, hour, minute)
    meds_window = Medications.get_meds_window(MedList, current, offset)

    def displayPills(medlist: list):
        print(f'meds to take {json.dumps(medlist, indent=2)}\n')

    # displayPills(meds_within_the_hour)
    displayPills(meds_at_specific_min)

    displayPills(meds_before)
    displayPills(meds_current)
    displayPills(meds_after)
    displayPills(meds_window)
