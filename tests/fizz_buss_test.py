import unittest
from src.fizz_buzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    

    def test_returns_fizz_if_divisible_by_3(self):
        self.assertEqual("Fizz", FizzBuzz.fizzbuzz(3))

    def test_returns_buzz_if_divisible_by_5(self):
        self.assertEqual("Buzz", FizzBuzz.fizzbuzz(5))

    def test_returns_fizzbuzz_if_divisible_by_3_and_5(self):
        self.assertEqual("FizzBuzz", FizzBuzz.fizzbuzz(15))

    def test_returns_input_if_not_divisible_by_5_or_3(self):
        self.assertEqual("1", FizzBuzz.fizzbuzz(1))