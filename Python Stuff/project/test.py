import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
    
# When testing I found that if all tests succeed it says that it ran 2 tests in a certain amount of time but if one fails it says
# that there was a error in it and it says where it was. The test results tell you if the numbers that you put in match what you
# expect the output to be.