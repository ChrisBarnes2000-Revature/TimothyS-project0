import unittest
from Clients.SampleClientMedList import MedList
import Medications


class TestEndcodeImage(unittest.TestCase):

    def test_get_monday_meds(self):
        self.assertDictEqual(
            MedList["MONDAY"]["1200"], {"Pill C"})

    def test_get_all_noon_and_midnight_meds(self):
        pass


if __name__ == '__main__':
    unittest.main()
