import unittest
from solution import count_less_than

class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
        target = 5
        self.assertEqual(count_less_than(matrix, target), 10)

    def test_2(self):
        matrix = [[1]]
        target = 1
        self.assertEqual(count_less_than(matrix, target), 0)

    def test_3(self):
        matrix = [[1, 2], [2, 3]]
        target = 2
        self.assertEqual(count_less_than(matrix, target), 1)

    def test_4(self):
        matrix = [[-10, -5, 0, 5], [0, 5, 10, 15], [10, 15, 20, 25], [20, 25, 30, 35]]
        target = 5
        self.assertEqual(count_less_than(matrix, target), 4)

    def test_5(self):
        matrix = [[1000000, 1000000], [1000000, 1000000]]
        target = 1000000
        self.assertEqual(count_less_than(matrix, target), 0)

    def test_6(self):
        matrix = [[1, 2, 4, 8, 16], [2, 4, 8, 16, 32], [4, 8, 16, 32, 64], [8, 16, 32, 64, 128], [16, 32, 64, 128, 256]]
        target = 100
        self.assertEqual(count_less_than(matrix, target), 22)

    def test_7(self):
        matrix = [[2, 3, 5, 7], [3, 5, 7, 11], [5, 7, 11, 13], [7, 11, 13, 17]]
        target = 10
        self.assertEqual(count_less_than(matrix, target), 10)

    def test_8(self):
        matrix = [[0, 10, 20, 30], [10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60]]
        target = 25
        self.assertEqual(count_less_than(matrix, target), 6)


if __name__ == "__main__":
    unittest.main()