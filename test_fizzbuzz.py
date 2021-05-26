import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz.fizz_buzz(1), "1")
    def test_3(self):
        self.assertEqual(fizzbuzz.fizz_buzz(3), "Fizz")
    def test_5(self):
        self.assertEqual(fizzbuzz.fizz_buzz(5), "Buzz")
    def test_15(self):
        self.assertEqual(fizzbuzz.fizz_buzz(15), "FizzBuzz")
    def test_all(self):
        self.assertEqual(fizzbuzz.fizz_buzz_100(), "12Fizz4BuzzFizz78Fizz"+\
        "Buzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829Fizz"+\
        "Buzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49Buzz"+\
        "Fizz5253FizzBuzz56Fizz5859FizzBuzz6162Fizz64BuzzFizz6768FizzBuzz71"+\
        "Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz91"+\
        "92Fizz94BuzzFizz9798FizzBuzz")
if __name__ == "__main__":
    unittest.main()