from typing import List

def is_toeplitz(matrix: List[List[int]]) -> bool:
   for i in range(len(matrix)-1):
      for j in range(len(matrix)-1):
         if matrix[i][j] != matrix[i+1][j+1]:
            return False
   return True