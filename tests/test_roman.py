from algorithms.roman import to_roman
import unittest


class RomanTestCase(unittest.TestCase):
    def test_numerals(self):
        self.assertEqual("I", to_roman(1))
        self.assertEqual("VIII", to_roman(8))
        self.assertEqual("IV", to_roman(4))
        self.assertEqual("VII", to_roman(7))
        self.assertEqual("XV", to_roman(15))
        self.assertEqual("MMXIV", to_roman(2014))
        self.assertEqual("MCMLIV", to_roman(1954))
