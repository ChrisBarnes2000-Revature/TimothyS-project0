import json
import sys
from datetime import datetime
from random import randint

# https://strftime.org/


def get_current_time():
    prompt = 'Please enter the current time in 24-hour format (0000-2359): '
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
        verbose and print(f'check2: {str(time_range[0]).zfill(4)} <= {res} >= {time_range[1]}')
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
        if current_day not in Utils["days_of_week"]:
            raise ValueError('Not An Acceptable Day Of The Week')
    except (ValueError, IndexError):
        exit(f'Not An Acceptable Day Of The Week\nPlease Use One Of {Utils["days_of_week"]}')
    return current_day


def convert_time_12hr(time_in_24hr: str):
    return datetime.strptime(time_in_24hr, "%H:%M").strftime("%I:%M %p")


def convert_time_24hr(time_in_12hr: str):
    return datetime.strptime(time_in_12hr, "%H:%M").strftime("%I:%M %H")


def create_new_client(name: str):
    name = name.capitalize()
    medlist = {}
    # for day in ["MONDAY", "TUSEDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]:
    for day in Utils["days_of_week"]:
        medlist[day] = {}
        # for hour in ["0000", "0100", "0200", "0300", "0400", "0500", "0600", "0700", "0800", "0900", "1000", "1100", "1200",
        #              "1100", "1200", "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300"]:
        for hour in Utils["hours_24_clock"]:
            medlist[day][hour] = {}
            for min in range(0, 60):
                medlist[day][hour][min] = {"Pill_Name": "More Info To Come"}

    # medlist = {day for day in Utils["days_of_week"]}
    # medlist[day] = {hour for hour in Utils["hours_24_clock"]}
    # medlist[day][hour] = {min for min in range(0, 60)}
    # medlist[day][hour][min] = {}

    sys.stdout = open(f'{name}.py', 'w')
    print(f'{name}_MedList = {json.dumps(medlist, indent=2)}')
    sys.stdout.close()


Utils = {
    "days_of_week": ["MONDAY", "TUSEDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"],
    "hours_24_clock":
        ["0000", "0100", "0200", "0300", "0400", "0500", "0600", "0700", "0800", "0900", "1000", "1100", "1200",
         "1100", "1200", "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300"],
    "get_current_day": get_current_day,
    "get_current_time": get_current_time,
    "convert_time_12hr": convert_time_12hr,
    "convert_time_24hr": convert_time_24hr,
    "create_new_client": create_new_client,
}
