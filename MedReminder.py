# Medication reminder program by Timothy S.
# Purpose is to remind user of what medications to take at specific time on the day of the week

from Clients.TimothyMedList import MedList
from operator import itemgetter
import Medications
import datetime


def get_current_time():
    acceptable_time = [0000, 2359]
    try:
        current_time = int(input('Please enter the current time in 24-hour format: '))
        if (current_time >= acceptable_time[1]) and (current_time <= acceptable_time[0]):
            raise ValueError('Not An Acceptable Time In 24 Hours')
    except (ValueError, IndexError):
        exit('Could not complete request.')
    return str(current_time)


def get_current_day():
    try:
        current_day = str(input('Please type the current day of the week: '))
        if current_day.upper() not in Medications.days_of_week:
            raise ValueError('Not An Acceptable Day Of The Week')
    except (ValueError, IndexError):
        exit('Could not complete request.')
    return current_day.upper()


if __name__ == '__main__':
    # Start of program
    print('Hello and welcome to your medication reminder!')

    # Input day of the week and current time
    current_day = get_current_day()
    current_time = get_current_time()

    # Searching for medications to be taken at inputted day and time
    current_meds = Medications.get_meds(MedList, current_day, current_time)
    print(
        f'Here are your prescribed medications for {current_day} at {current_time}:\n {current_meds}')
    print("\n-----------\n")
    Medications.get_monday_meds(MedList)
    print("\n-----------\n")
    Medications.get_all_noon_and_midnight_meds(MedList)
