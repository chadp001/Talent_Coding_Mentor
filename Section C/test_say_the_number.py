import unittest
from say_number import say_the_number

class TestNumberToText(unittest.TestCase):
    def test_say_the_number_zero(self):
        self.assertEquals(say_the_number(0), "Zero.")

    def test_say_the_number_eleven(self):
        self.assertEquals(say_the_number(11), "Eleven.")

    def test_say_the_number_fourteen(self):
        self.assertEquals(say_the_number(14), "Fourteen.")

    def test_say_the_number_fifteen(self):
        self.assertEquals(say_the_number(15), "Fifteen.")

    def test_say_the_number_forty_three(self):
        self.assertEquals(say_the_number(43), "Forty-three.")

    def test_say_the_number_fifty(self):
        self.assertEquals(say_the_number(50), "Fifty.")

    def test_say_the_number_one_thousand_and_one(self):
        self.assertEquals(say_the_number(1001), "One thousand and one.")

    def test_say_the_number_twenty_thousand(self):
        self.assertEquals(say_the_number(20000), "Twenty thousand.")

    def test_say_the_number_one_million_thirty_three_thousand_two_hundred_and_eighty_six(self):
        self.assertEquals(say_the_number(1033286), "One million, thirty-three thousand, two hundred and eighty-six.")

    def test_say_the_number_twelve_million_and_thirteen(self):
        self.assertEquals(say_the_number(12000013), "Twelve million and thirteen.")

    def test_say_the_number_ninety_trillion_three_hundred_and_seventy_six_billion_ten_thousand_and_twelve(self):
        self.assertEquals(say_the_number(90376000010012), "Ninety trillion, three hundred and seventy-six billion, ten thousand and twelve.")


if __name__ == '__main__':
    unittest.main()