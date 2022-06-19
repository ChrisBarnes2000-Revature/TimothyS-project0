# Data Structures containing prescribed medications and their day and time to be taken (Time to take medication: Medications prescribed)
# Moved To Clients.SampleMedList -->
#       from Clients.SampleClientMedList import MedList
#       from Clients.TimothyMedList import MedList
#       from Clients.ChrisMedList import MedList

from Clients.SampleClientMedList import MedList


days_of_week = ["MONDAY", "TUSEDAY", "WEDNESDAY",
                "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]


# def get_monday_meds(medlist):
#     for hour in range(24):
#         hour_24 = "0"+str(hour)+"00" if hour < 10 else str(hour)+"00"
#         monday_meds_by_hour = medlist["MONDAY"][hour_24]
#         print(f'The Time Is: {hour}, Take These Meds:\n{monday_meds_by_hour}')


# def get_all_noon_and_midnight_meds(medlist):
#     for day in days_of_week:
#         noon_meds = medlist[day]["1200"]
#         midnight_meds = medlist[day]["0000"]
#         print(f'At Noon On {day} Take These Meds:\n{noon_meds}\n')
#         print(f'At Midnight On {day} Take These Meds:\n{midnight_meds}\n')


# Function that returns the prescribed medications on the given day and time
def get_meds(medlist, day, time):
    # Returning prescribed medications to take on given time (fitting in time range of two hours before and after) and day
    return medlist[day][time]
