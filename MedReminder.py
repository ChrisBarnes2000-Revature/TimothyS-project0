# Medication reminder program by Timothy S.
# Purpose is to remind user of what medications to take at specific time on the day of the week

from Clients.TimothyMedList import MedList
from operator import itemgetter
import Medications
import datetime

if __name__ == '__main__':
    # Start of program
    print('Hello and welcome to your medication reminder!')

    # Input day of the week and current time
    current_day = str(input('Please type the current day of the week: '))
    current_time = str(
        input('Please enter the current time in 24-hour format: '))

    Medications.get_monday_meds(MedList)
    print("\n-----------\n")
    Medications.get_all_noon_and_midnight_meds(MedList)
    print("\n-----------\n")
    # Searching for medications to be taken at inputted day and time
    current_meds = Medications.get_meds(MedList, current_day, current_time)
    print(
        f'Here are your prescribed medications for {current_day} at {current_time}:\n {current_meds}')

    # for day in days_of_the_week:
    #     if current_day == day:
    #         print('Here are your prescribed medications for ' +
    #               day + ' at ' + current_time + ":")
    #         print(get_meds(current_day, current_time))
