import unittest
from solution11 import second_max

class TestSecondMax(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(second_max([3, 2, 1]), 2)
        
    def test_case_2(self):
        self.assertEqual(second_max([1, 2, 3, 2, 1]), 2)
        
    def test_case_3(self):
        self.assertEqual(second_max([1000000, -1000000, 500000]), 500000)
        
    def test_case_4(self):
        self.assertEqual(second_max([10, 10, 10, 10]), None)
        
    def test_case_5(self):
        self.assertEqual(second_max([999999, 1000000]), 999999)
        
    def test_case_6(self):
        self.assertEqual(second_max([1]), None)
        
    def test_case_7(self):
        self.assertEqual(second_max([]), None)
        
    def test_case_8(self):
        self.assertEqual(second_max([5, 3, 4]), 4)
        
    def test_case_9(self):
        self.assertEqual(second_max([0, 0, 0, 0, 0, -1]), -1)

    def test_case_10(self):
        self.assertEqual(second_max([1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5]), 4)

if __name__ == '__main__':
    unittest.main()