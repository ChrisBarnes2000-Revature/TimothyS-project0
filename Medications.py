from Utils import Utils


def get_patient(name: str):
    """
    Get the entire medlist of the given patient
    Params:
        name (str): A string representing the name of the patient in query
    Return:
        meds (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
    """
    if name == "Grandma-Test":
        from Clients.TestClients.Grandma import Grandma_MedList as MedList
    elif name == "Father-Test":
        from Clients.TestClients.Father import Father_MedList as MedList
    elif name == "Lizzy-Test":
        from Clients.TestClients.Lizzy import Lizzy_MedList as MedList
    else:
        from Clients.SampleClientMedList import MedList
    return MedList


def get_meds_today(medlist: dict, today: str):
    """
    Get the patient's prescribed medications on a given day & time
    Params:
        medlist (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
        day      (str): A string representing the day of the week the user would like to check for medication on
    Return:
        meds    (list): A List containing the sub dicts of time of the given day
    """
    return medlist[today.upper()]


def get_meds_hourly(today: str):
    for hour in range(24):
        hour_24 = "0"+str(hour)+"00" if hour < 10 else str(hour)+"00"
        current_hour_meds = get_meds_today(today)[hour_24]
        print(f'The Time Is: {hour}:{"00"}, Take These Meds:\n{current_hour_meds}')
        yield current_hour_meds


def get_meds_by_minute(today: str):
    for minute in range(60):
        current_hour = get_meds_hourly(today)
        current_minute_meds = current_hour[minute]
        print(f'The Time Is: {current_hour}:{minute}, Take These Meds:\n{current_minute_meds}')
        yield current_minute_meds


def get_current_meds(medlist: list, today: str, hour: str, minute: str = None):
    """
    Get the patient's prescribed medications on a given day & time
    Params:
        day     (str): A string representing the day of the week the user would like to check for medication on
        hour    (int): An integer representing the hour in the day at which the user needs or expects to take meds
        minute  (int): An integer representing the minute in the hour at which ...
    Return:
        meds   (dict): A dict containing the meds to take in the given minute
    """
    if minute != None:
        return get_meds_today(medlist, today)[str(hour)][str(int(minute))]
    else:
        return get_meds_today(medlist, today)[str(hour)]


def get_meds_before(medlist: list, current: list, offset: list):
    before_hrs = int(current[1]) - int(offset[0])
    before_min = int(current[2]) - int(offset[1])
    return get_current_meds(medlist, current[0], before_hrs, before_min)


def get_meds_after(medlist: list, current: list, offset: list):
    after_hrs = int(current[1]) + int(offset[0])
    after_min = int(current[2]) + int(offset[1])
    return get_current_meds(medlist, current[0], after_hrs, after_min)


def get_meds_window(medlist: list, current: list, offset: list):
    # def get_meds_window(MedList, current_day, current_time, offset="0200"):
    """
    Because medications can still be taken "2 hours" before or after the planned time,
        * we want it to display a dict containing the range of time "2 hours" before through "2 hours" after the inputted time
        * we want it to display the "exact" time -- {hour}:{minute}
    Example output is expected to be
        Here's your meds for Monday at 1430 meds:{1230:{},1430: {"Multi-Vitamins": "More Info To Come"},1630: {}}
        or
        > Here's your meds for Monday at 1430
        > meds: {
        >   1030: {},
        >   1230: {"Multi-Vitamins": "More Info To Come"},
        >   1430: {}
        > }
    Params:
        time    (str): A string representing the time of day the user would like to check for medication at
        offset  (str): A string representing the number of hours to offset our acceptable list of current meds
    Return:
        meds   (list): A list of sub dicts within the time range of (XX time) before & after current time
    """
    # current_time_plus_1 = str(int(current_time)+100)
    # current_time_plus_2 = str(int(current_time)+200)

    # current_time_minus_1 = str(int(current_time)-100)
    # current_time_minus_2 = str(int(current_time)-200)

    # # Searching for medications to be taken at inputted day and time
    # print(f''''Here are your prescribed medications for {current_day} at {current_time}:
    #     { Medications.get_meds(MedList, current_day, Utils["get_current_time_sub_12"](current_time_minus_2)) }
    #     { Medications.get_meds(MedList, current_day, Utils["get_current_time_sub_12"](current_time_minus_1)) }

    #     { Medications.get_meds(MedList, current_day, Utils["get_current_time_sub_12"](current_time)) }

    #     { Medications.get_meds(MedList, current_day, Utils["get_current_time_sub_12"](current_time_plus_1)) }
    #     { Medications.get_meds(MedList, current_day, Utils["get_current_time_sub_12"](current_time_plus_2)) }
    # ''')
    # current = ["day", "hour", "minute"]
    before__meds = get_meds_before(medlist, current, offset)
    current_meds = get_current_meds(medlist, current[0], current[1], current[2])
    after___meds = get_meds_after(medlist, current, offset)
    return before__meds, current_meds, after___meds


def get_all_noon_and_midnight_meds(medlist):
    for day in Utils["days_of_week"]:
        noon_meds = medlist[day]["1200"]
        midnight_meds = medlist[day]["0000"]
        print(f'At Noon On {day} Take These Meds:\n{noon_meds}\n')
        print(f'At Midnight On {day} Take These Meds:\n{midnight_meds}\n')
        return midnight_meds, noon_meds
