def solution(nums):
    even_count,odd_count = 0,0
    for i in nums:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return(even_count,odd_count)