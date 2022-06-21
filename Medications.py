from Clients.SampleClientMedList import MedList
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
    return MedList


def get_meds_today(medlist: dict, day: str):
    """
    Get the patient's prescribed medications on a given day & time
    Params:
        medlist (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
        day      (str): A string representing the day of the week the user would like to check for medication on
    Return:
        meds    (list): A List containing the sub dicts of time of the given day
    """
    pass


def get_current_meds(day: str, hour: int, minute: int):
    """
    Get the patient's prescribed medications on a given day & time
    Params:
        day     (str): A string representing the day of the week the user would like to check for medication on
        hour    (int): An integer representing the hour in the day at which the user needs or expects to take meds
        minute  (int): An integer representing the minute in the hour at which ...
    Return:
        meds   (dict): A dict containing the meds to take in the given minute
    """
    pass


def get_meds_window(MedList, current_day, current_time, offset="0200"):
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
    pass
