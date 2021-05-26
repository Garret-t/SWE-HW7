import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz.fizz_buzz(1), "1")
    def test_3(self):
        self.assertEqual(fizzbuzz.fizz_buzz(3), "Fizz")
        
if __name__ == "__main__":
    unittest.main()