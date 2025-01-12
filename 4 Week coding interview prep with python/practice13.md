You're given a matrix where each row is sorted in ascending order. The columns are also sorted in ascending order. This creates a special pattern where the values in the matrix increase as you move right or down but decrease as you move left or up.

Your task is to write a Python function that counts the number of integers in the matrix that are smaller than the given target. The function should return this count as an integer.

The expected complexity is 
O
(
n
+
m
)
O(n+m), where 
n
n is the number of rows and 
m
m is the number of columns in the matrix.

For example, given a matrix:

Copy to clipboard
[
  [1, 2, 3, 4],
  [2, 3, 4, 5],
  [3, 4, 5, 6],
  [4, 5, 6, 7]
]
and a target of 5, the function count_less_than(matrix, 5) should return 10 because there are 10 numbers in the matrix that are less than 5.