import random
import unittest

import Medications
import MedReminder
from Clients.SampleClientMedList import MedList as test_meds_0
from Clients.TestClients.Grandma import Grandma_MedList as test_meds_1
from Clients.TestClients.Father import Father_MedList as test_meds_2
from Clients.TestClients.Lizzy import Lizzy_MedList as test_meds_3
from Utils import Utils


class TestMedReminder(unittest.TestCase):

    print("Start MedReminder Tests")

    def test_should_do_something(self):
        self.assertTrue(True)
        print("MedReminder Test Method: Sample \t\t| Completed")

    """ Example User Test Cases
        * Grandma needs to take her meds
            - 3 times on monday wednesday & friday
            - 2 time on tuseday & thursday
            - random times on saturday & sunday
        * Father needs to take his meds
            - 2 times on monday & thursday
            - 1 times - anytime as needed
        * Lizzy needs to take their meds
            - 1 time daily
    """

    """
    Because medications can still be taken "2 hours" before or after the planned time,
        * we want it to display a dict containing the range of time "2 hours" before through "2 hours" after the inputted time
        * we want it to display the "exact time -- {hour}:{minute}"

    Example run:
        $ python3 MedReminder.py
        > Hello and welcome to your medication reminder!
        > Please type the current day of the week:                      $ Monday
        > Please enter the current time in 24-hour format (0000-2359):  $ 1230

    Output should be:
        > Here's your meds for Monday at 1430 meds:{1230:{},1430: {"Multi-Vitamins": "More Info To Come"},1630: {}}
        or
        > Here's your meds for Monday at 1430
        > meds: {
        >   1030: {},
        >   1230: {"Multi-Vitamins": "More Info To Come"},
        >   1430: {}
        > }
    """

    """ Example Medlist
    MedList: {
        "SUNDAY": { "1200": {}, },
        "MONDAY": {
            "0600": {"pill_a": "More Info To Come"},
            "1200": {"pill_b": "More Info To Come"},
            "1800": {"pill_c": "More Info To Come"},
        },
        "TUSEDAY": {
            "1200": {"Multi-Vitamins": "More Info To Come"},
            "1800": {"Multi-Vitamins": "More Info To Come"},
        },
        "WEDNESDAY": {
            "0600": {"pill_a": "More Info To Come"},
            "1200": {"pill_b": "More Info To Come"},
            "1800": {"pill_c": "More Info To Come"},
        },
        "THURSDAY": {
            "1200": {"Multi-Vitamins": "More Info To Come"},
            "1800": {"Multi-Vitamins": "More Info To Come"},
        },
        "FRIDAY": {
            "0600": {"pill_a": "More Info To Come"},
            "1200": {"pill_b": "More Info To Come"},
            "1800": {"pill_c": "More Info To Come"},
        },
        "SATURDAY": {
            1200": {
                "Multi-Vitamins": "More Info To Come",
                "Iron": "More Info To Come",
                "Zinc": "More Info To Come"
            }
        },
    }
    """

    """ Example Test Cases
        IS_EMPTY():
            Check entire Medlsit
            Check each day in MedList
            Check each hour in each day
            Check each minute in every hour
        HAS_CORRECT_OUTPUT_VALUE():
            Check output value is correct
            Check with false data to be incorrect
        HAS_CORRECT_DISPLAY():
            Check output text is correct
            Check output value is correct
    """

    # --------------------------- #

    # no_pill_options = {}
    # all_pill_options = {"Multi-Vitamins", "Iron", "Zinc", "Magnesium", "Calcium", "Vitamin B-12", "Vitamin D", "pill_a", "pill_b", "pill_c"}

    # lizzy_pill_options = {"Multi-Vitamins"}
    # father_pill_options = {"Multi-Vitamins", "Iron", "Zinc", "Magnesium", "Calcium", "Vitamin B-12", "Vitamin D"}
    # grandma_pill_options = {"Multi-Vitamins", "pill_a", "pill_b", "pill_c"}

    # time = "1430"
    # hour = int(str(res)[:2]) + "00"   # 1400
    # minute = int(str(res)[2:])        # 30
    # expected_output = # ... Algorithim Comming Soon

    # self.assertDictEqual(MedList[day][time], expected_output)
    # self.assertDictEqual(Medications.get_current_meds(day, hour, minute, expected_output)

    # --------------------------- #
    class TestUserInput(unittest.TestCase):

        print("Start User Input Tests")

        def test_should_do_something(self):
            self.assertTrue(True)
            print("User Input Test Method: Sample \t\t| Completed")

        def test_get_current_day(self):
            """
            Test we get the corret response from user when requesting a day of the week
            they are prompted "Please type the current day of the week: "
            output is expected to be one of ["SUNDAY", "MONDAY", "TUSEDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
            Params:
                day (str): string representing the day of the week the user would like to check for medication on
            Return:
                day (str): ALL CAPS Version of the day provided by the user
            """
            print("User Input Test Method: Get Current Day \t| Started")
            print("User Input Test Method: Get Current Day \t| Completed\n")

        def test_get_current_time(self):
            """
            Test we get the corret response from user when requesting a time of day
            they are prompted "Please enter the current time in 24-hour format(0000-2359): "
            output is expected to be one of ["0000", "0100", 0200", ..., "2100", "2200", "2300"]
            Params:
                time (str): string representing the time of day the user would like to check for medication at
            Return:
                time (str): string version of verified number in range of the 24 hour clock
            """
            print("User Input Test Method: Get Current Time \t| Started")
            print("User Input Test Method: Get Current Time \t| Completed\n")

    class TestMedList(unittest.TestCase):

        print("Start Med List Tests")

        def test_should_do_something(self):
            self.assertTrue(True)
            print("Med List Test Method: Sample \t\t\t| Completed\n")

        def test_get_patient(self):
            """
            Test we get the entire medlist of the given user
            Params:
                name (str): A string representing the name of the patient in query
            Return:
                meds (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
            """
            print("Med List Test: Get Patient \t\t\t| Started")
            # Test Case 1 -- Grandma
            expexted_test_data = test_meds_1
            our_method_results = Medications.get_patient(name="Grandma-Test")
            error_message = f'Error Result are not what we want\nExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 2 -- Father
            expexted_test_data = test_meds_2
            our_method_results = Medications.get_patient(name="Father-Test")
            error_message = f'Error Result are not what we want\nExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 3 -- Lizzy
            expexted_test_data = test_meds_3
            our_method_results = Medications.get_patient(name="Lizzy-Test")
            error_message = f'Error Result are not what we want\nExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)
            print("Med List Test Method: Get Patient \t\t| Completed\n")

        def test_get_meds_today(self):
            """
            Test we get the correct list of meds from the given medlist provided a day to index
            Params:
                medlist (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
                day      (str): A string representing the day of the week the user would like to check for medication on
            Return:
                meds    (list): A List containing the sub dicts of time of the given day
            """
            print("Med List Test: Get Meds Today \t\t\t| Started")
            today = random.choice(Utils["days_of_week"])

            # Test Case 1 -- Grandma
            expexted_test_data = test_meds_1[today]
            medlist = Medications.get_patient(name="Grandma-Test")
            our_method_results = Medications.get_meds_today(medlist, today)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 2 -- Father
            expexted_test_data = test_meds_2[today]
            medlist = Medications.get_patient(name="Father-Test")
            our_method_results = Medications.get_meds_today(medlist, today)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 3 -- Lizzy
            expexted_test_data = test_meds_3[today]
            medlist = Medications.get_patient(name="Lizzy-Test")
            our_method_results = Medications.get_meds_today(medlist, today)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)
            print("Med List Test Method: Get Meds Today \t\t| Completed\n")

        def test_get_meds_hourly(self):
            """
            Test we get the correct list of meds from the given medlist provided a day to index
            Params:
                medlist      (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
                day           (str): A string representing the day of the week the user would like to check for medication on
            Yield:
                meds         (dict): A dict containing the meds to take in the given hour
                    i.e if at midnight (0000) you had to take 3 pills it may look like:
                    { "Multi-Vitamins": "More Info To Come", "Iron": "More Info To Come", "Zinc": "More Info To Come" }
            """
            print("Med List Test Method: Get Med Hourly \t\t| Started")
            print("Med List Test Method: Get Med Hourly \t\t| Completed\n")

        def test_get_meds_by_minute(self):
            """
            Test we get the correct list of meds from the given medlist provided a day to index
            Params:
                medlist      (dict): A dict of dicts containg the users medication used as --> meds[day][hour][minute] --> {"Multi-Vitamins": "More Info To Come"},
                day           (str): A string representing the day of the week the user would like to check for medication on
            Yield:
                meds         (dict): A dict containing the meds to take in the given minute
                    i.e if at lunch (1030 or 1230) you had to take 1 pill it may look like:
                    { "Multi-Vitamins": "More Info To Come" }
            """
            print("Med List Test Method: Get Meds By Minute \t| Started")
            print("Med List Test Method: Get Meds By Minute \t| Completed\n")

        def test_get_current_meds(self):
            """
            Test we get the correct list of meds from the given medlist provided a day & time (hour, minute) to index
            Params:
                day     (str): A string representing the day of the week the user would like to check for medication on
                hour    (int): An integer representing the hour in the day at which the user needs or expects to take meds
                minute  (int): An integer representing the minute in the hour at which ...
            Return:
                meds   (dict): A dict containing the meds to take in the given minute
                    i.e if at dinner (1730 or 1800) you had to take 2 pill it may look like:
                    { "Iron": "More Info To Come", "Zinc": "More Info To Come" }
            """
            print("Med List Test Method: Get Current Meds \t\t| Started")
            today = "MONDAY"  # random.choice(Utils["days_of_week"])
            hour = "1200"  # random.choice(Utils["hours_24_clock"])
            minute = "30"  # random.randint(0, 60)

            # Test Case 0 -- Sample Client
            expexted_test_data = test_meds_0[today][hour][minute] if minute != '' else test_meds_0[today][hour]
            our_method_results = Medications.get_current_meds(test_meds_0, today, hour, minute)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 1 -- Grandma
            expexted_test_data = test_meds_1[today][hour][minute] if minute != '' else test_meds_1[today][hour]
            our_method_results = Medications.get_current_meds(test_meds_1, today, hour, minute)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 2 -- Father
            expexted_test_data = test_meds_2[today][hour][minute] if minute != '' else test_meds_2[today][hour]
            our_method_results = Medications.get_current_meds(test_meds_2, today, hour, minute)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)

            # Test Case 3 -- Lizzy
            expexted_test_data = test_meds_3[today][hour][minute] if minute != '' else test_meds_3[today][hour]
            our_method_results = Medications.get_current_meds(test_meds_3, today, hour, minute)
            error_message = f'Error Result are not what we wantExpected: {expexted_test_data} | Actual: {our_method_results}'
            self.assertDictEqual(our_method_results, expexted_test_data, error_message)
            print("Med List Test Method: Get Current Meds \t\t| Completed\n")

        def test_get_meds_before(self):
            """
            Test we get the correct list of meds from the given medlist provided a day & time (hour, minute) & offset to index
            Params:
                day      (str): A string representing the day of the week the user would like to check for medication on
                time    (list): [hour: (int), minute, (int)] - Integer representing the hour & minute in the day at which the user needs or expects to take meds
                offset   (int): An integer representing the number of hours to offset our acceptable list of current meds
            Return:
                meds    (dict): A dict containing the meds to take in the given time frame (prior to current set)
            """
            print("Med List Test Method: Get Meds Before \t\t| Started")
            print("Med List Test Method: Get Meds Before \t\t| Completed\n")

        def test_get_meds_after(self):
            """
            Test we get the correct list of meds from the given medlist provided a day & time (hour, minute) & offset to index
            Params:
                day      (str): A string representing the day of the week the user would like to check for medication on
                time    (list): [hour: (int), minute, (int)] - Integer representing the hour & minute in the day at which the user needs or expects to take meds
                offset   (int): An integer representing the number of hours to offset our acceptable list of current meds
            Return:
                meds    (dict): A dict containing the meds to take in the given time frame (after current set)
            """
            print("Med List Test Method: Get Meds After \t\t| Started")
            print("Med List Test Method: Get Meds After \t\t| Completed\n")

        def test_get_meds_window(self):
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
                time (str): string representing the time of day the user would like to check for medication at
            Return:
                meds (dict): a dict containing the sub dicts within the time range of (XX time) before & after current time
            """
            print("Med List Test Method: Get Meds Window \t\t| Started")
            print("Med List Test Method: Get Meds Window \t\t| Completed\n")

    def test_XXX(self):
        """
        Summary Line
        Extra Details
        Params:
        Return:
        """
        pass

    def test_XXX(self):
        """
        Summary Line
        Extra Details
        Params:
        Return:
        """
        pass

    def test_inner_test_class(self):
        suite_1 = unittest.defaultTestLoader.loadTestsFromTestCase(self.TestUserInput)
        suite_2 = unittest.defaultTestLoader.loadTestsFromTestCase(self.TestMedList)
        print()
        unittest.TextTestRunner().run(suite_1)
        unittest.TextTestRunner().run(suite_2)


if __name__ == '__main__':
    unittest.main()
