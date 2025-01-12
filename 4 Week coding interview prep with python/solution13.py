def count_less_than(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    count_less = 0
    
    row, col = 0, m-1
    while row < n and col >=0 : 
        if matrix[row][col] < target:
            count_less += col + 1
            row += 1
        else:
            col -= 1
    return count_less
            
        