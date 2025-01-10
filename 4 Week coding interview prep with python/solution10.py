def count_min(numbers):
    if not numbers:
        return 0
    min_num = numbers[0]
    count_min = 0
    for i in numbers:
        if min_num > i:
            min_num = i
            count_min = 1
        elif min_num == i:
            count_min += 1
    return count_min
            
        