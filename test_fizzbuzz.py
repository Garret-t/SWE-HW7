import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz.fizz_buzz(1), "1")

if __name__ == "__main__":
    unittest.main()