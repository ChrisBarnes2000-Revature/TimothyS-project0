# Medication reminder program by Timothy S.
# Purpose is to remind user of what medications to take at specific time on the day of the week

from Clients.TimothyMedList import MedList
from operator import itemgetter
import Medications
import datetime


def get_current_time():
    prompt = 'Please enter the current time in 24-hour format: '
    prompt2 = 'Please Use 24 Hour Time Format (0000 - 2359)'

    response = input(prompt)
    time_range = [0000, 2359]
    hour_range = [00, 23]
    minute_range = [00, 59]
    verbose = False

    # Did they enter a numbr
    def check1(res):
        verbose and print("check1:")
        return res.isnumeric()

    # Is the said number out of range of the 24 hour clock (first is it below 0000) (second is to above 2359)
    def check2(res):
        given_time = int(res)
        verbose and print(
            f'check2: {str(time_range[0]).zfill(4)} <= {res} >= {time_range[1]}')
        return given_time >= time_range[0] and given_time <= time_range[1]

    # Are the first 2 digits in said number out of range of the 24 hour clock (first is it below 00) (second is to above 23)
    def check3(res):
        hour = int(str(res)[:2])
        verbose and print("check3:")
        return not ((hour <= hour_range[0]) and (hour >= hour_range[1]))

    # Are the last 2 digits in said number out of range of the 24 hour clock (first is it below 00) (second is to above 59)
    def check4(res):
        minute = int(str(res)[2:])
        verbose and print("check4:")
        return not ((minute <= minute_range[0]) and (minute >= minute_range[1]))

    def isValid(response):
        return check1(response) and check2(response) and check3(response) and check4(response)

    while not isValid(response):
        response = input(f'Try again: {prompt2}')

    # Return str(response) If You Want To Have Specification Over Every Minute Rather Than Hours
    hour = str(response)[:2]
    return hour + "00"


def get_current_day():
    try:
        current_day = str(
            input('Please type the current day of the week: ')).upper()
        if current_day not in Medications.days_of_week:
            raise ValueError('Not An Acceptable Day Of The Week')
    except (ValueError, IndexError):
        exit(
            f'Not An Acceptable Day Of The Week\nPlease Use One Of {Medications.days_of_week}')
    return current_day


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
