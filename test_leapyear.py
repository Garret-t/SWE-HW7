import unittest
import leapyear

class TestLeapYear(unittest.TestCase):
    def test_3(self):
        self.assertEqual(leapyear.is_leapyear(3), False)

if __name__ == "__main__":
    unittest.main()