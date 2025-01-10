from typing import List, Optional

def second_max(nums: List[int]) -> Optional[int]:
    if len(set(nums)) < 2:
        return None
    
    max_num, second_max_num = float('-inf'), float('-inf')
    
    for i in nums:
        if max_num is None or i > max_num:
            second_max_num = max_num
            max_num = i
        elif i != max_num and i > second_max_num:
            second_max_num = i 
            
    return second_max_num if second_max_num != float('-inf') else None