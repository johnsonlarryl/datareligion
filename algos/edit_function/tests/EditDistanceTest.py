import unittest
from EditDistance import EditDistance
from nltk.metrics.distance import edit_distance

class EditDistanceTest(unittest.TestCase):
    def setUp(self):
        self.distance = EditDistance()

    def testCalculate(self):
        # string1 = "shortString"
        # string2 = "aVeryLongString"
        string1 = "kitten"
        string2 = "sitting"
        expect_distance = 3
        actual_distance = self.distance.calculate(string1, string2)
        nltl_edit_distance = edit_distance(string1,string2)
        self.assertEqual(expect_distance, actual_distance)
        self.assertEqual(expect_distance, nltl_edit_distance)