import unittest

from calculator import calculate
from calculator import str_calculator

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)

    def test_odejmowanie(self):
        r = calculate(10, 5, '-')
        self.assertEqual(r, 5)

    def test_mnozenie(self):
        r = calculate(1,2,'*')
        self.assertEqual(r, 2)

    def test_dzielenie(self):
        r = calculate(4,2,'/')
        self.assertEqual(r, 2)

class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator ("a", "b", 'concat')
        self.assertEqual(r, 'ab')
