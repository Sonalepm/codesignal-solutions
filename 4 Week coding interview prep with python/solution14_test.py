import unittest
from solution import solution

class TestsSolution(unittest.TestCase):

    def test1(self):
        grid = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.assertEqual(solution(grid), [3, 15])

    def test2(self):
        grid = [[-5, -1, -9, -11], [-2, -4, -8, -10], [-13, -3, -6, -7], [-15, -14, -12, -16]]
        self.assertEqual(solution(grid), [-15, -3])

    def test3(self):
        self.assertEqual(solution([[0]]), [0, 0])

    def test4(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(solution(grid), [4, 13])

    def test5(self):
        grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        self.assertEqual(solution(grid), [1, 1])

    def test6(self):
        grid = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]
        self.assertEqual(solution(grid), [-13, -4])

    def test7(self):
        self.assertEqual(solution([]), [None, None])


if __name__ == '__main__':
    unittest.main()