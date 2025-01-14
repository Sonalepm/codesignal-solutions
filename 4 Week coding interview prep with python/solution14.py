
def solution(grid):
    if not grid:
        return ([None, None])
        
    max_value, min_value = float('-inf'), float('inf')
    size = len(grid)
    i = size - 1
    while i >= 0:
        if grid[size - 1 - i][i] > max_value:
            max_value = grid[size - 1 - i][i]
        if grid[size - 1 - i][i] < min_value :
            min_value = grid[size - 1 - i][i]
        i -= 1
        
    return ([min_value, max_value])
    
