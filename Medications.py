from calendar import week
from calendar import timegm
import datetime
from operator import itemgetter

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
# Data Structures containing prescribed medications and their day and time to be taken
# meds = {Med A: {days: ["Monday", "Wednesday", "Friday"], time: "0800"}, Med B: {days: ["Monday", "Wednesday"], time: "0800"}, Med C: {days: ["Tuesday, Thursday"], time: "0800"}
#        }
monday_meds = {(Pill A, Pill B, Pill C): 0800, (Pill A, Pill D): 1800}
tuesday_meds = {(Pill E, Pill F): 0800, (Pill E): 1800}
wednesday_meds = {(Pill A, Pill B, Pill C): 0800, (Pill A, Pill D): 1800}
thursday_meds = {(Pill E, Pill F): 0800, (Pill E): 1800}
friday_meds = {(Pill A, Pill B, Pill C): 0800, (Pill A, Pill D): 1800}
saturday_meds = {(Pill G): 0900, (Pill H): 2100}
sunday_meds = {(Pill G): 0900, (Pill H): 2100}


def get_meds(day, time):
    pass
