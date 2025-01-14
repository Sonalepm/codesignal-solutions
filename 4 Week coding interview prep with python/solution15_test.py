import unittest
from typing import List, Union
from solution import find_row_with_target


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_row_with_target([
            [1, 4, 7, 11],
            [2, 5, 8, 12],
            [3, 6, 9, 16]
        ], 9), 2)
        
    def test2(self):
        self.assertEqual(find_row_with_target([
            [-5, -3, 0, 3],
            [-2, 2, 7, 10]
        ], -5), 0)
        
    def test3(self):
        self.assertEqual(find_row_with_target([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], 5), 1)
        
    def test4(self):
        self.assertEqual(find_row_with_target([[100]], 100), 0)

    def test5(self):
        self.assertEqual(find_row_with_target([
            [1],
            [2],
            [3],
            [4],
            [5]
        ], 3), 2)
        
    def test6(self):
        self.assertIsNone(find_row_with_target([
            [1, 2, 3, 4, 5]
        ], 10))
        
    def test7(self):
        self.assertEqual(find_row_with_target([
            [-1000, -500],
            [-300, 10],
            [20, 1000]
        ], -300), 1)
        
    def test8(self):
        self.assertEqual(find_row_with_target([
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3]
        ], 2), 1)

    def test9(self):
        self.assertIsNone(find_row_with_target([
            [1, 4, 7, 11],
            [14, 15, 16, 20],
            [22, 23, 24, 30]
        ], 25))
        
    def test10(self):
        self.assertIsNone(find_row_with_target([
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ], 35))
        
    def test11(self):
        self.assertIsNone(find_row_with_target([
            [-10, -5, 0, 5],
            [10, 15, 20, 25]
        ], 6))

if __name__ == '__main__':
    unittest.main()