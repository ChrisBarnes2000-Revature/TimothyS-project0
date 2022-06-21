import unittest
from Clients.SampleClientMedList import MedList
from Clients.TestClients.Father import MedList as test_meds_1
from Clients.TestClients.Grandma import MedList as test_meds_2
from Clients.TestClients.Lizzy import MedList as test_meds_3
import Medications
import MedReminder


class TestMedReminder(unittest.TestCase):

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
        "SUNDAY": { "1200": {} },
        "MONDAY": {
            "0600": {"pill_a": "More Info To Come"}
            "1200": {"pill_b": "More Info To Come"}
            "1800": {"pill_c": "More Info To Come"}
        },
        "TUSEDAY": {
            "1200": {"Multi-Vitamins": "More Info To Come"},
            "1800": {"Multi-Vitamins": "More Info To Come"}
        },
        "WEDNESDAY": {
            "0600": {"pill_a": "More Info To Come"}
            "1200": {"pill_b": "More Info To Come"}
            "1800": {"pill_c": "More Info To Come"}
        },
        "THURSDAY": {
            "1200": {"Multi-Vitamins": "More Info To Come"},
            "1800": {"Multi-Vitamins": "More Info To Come"}
        },
        "FRIDAY": {
            "0600": {"pill_a": "More Info To Come"}
            "1200": {"pill_b": "More Info To Come"}
            "1800": {"pill_c": "More Info To Come"}
        },
        "SATURDAY": { "1200": {} }
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
            pass

        def test_get_current_time(self):
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

    def test_XXX(self):
        """
        Summary Line
        Extra Details
        Params:
        Return:
        """
        pass


# Example run:
# $ python3 MedReminder.py
# > Hello and welcome to your medication reminder!
# > Please type the current day of the week:                      $ Monday
# > Please enter the current time in 24-hour format(0000-2359):  $ 1230

# Output should be:
# > Here's your meds for Monday at 1430 meds:{1230:{},1430: {"Multi-Vitamins": "More Info To Come"},1630: {}}
# or
# > Here's your meds for Monday at 1430
# > meds: {
# >   1030: {},
# >   1230: {"Multi-Vitamins": "More Info To Come"},
# >   1430: {}
# > }

if __name__ == '__main__':
    unittest.main()
