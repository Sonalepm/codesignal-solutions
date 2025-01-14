def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
    if not matrix or not matrix[0]:
        return None
    rows = len(matrix)
    columns = len(matrix[0])
    row, col = 0, columns - 1
    while row >= 0 and row < rows and col >= 0:
        if target == matrix[row][col]:
            return (row)
        elif target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
    return (None)
             
            
            