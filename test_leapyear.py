import unittest
import leapyear

class TestLeapYear(unittest.TestCase):
    def test_3(self):
        self.assertEqual(leapyear.is_leapyear(3), False)
    def test_4(self):
        self.assertEqual(leapyear.is_leapyear(4), True)
        
if __name__ == "__main__":
    unittest.main()