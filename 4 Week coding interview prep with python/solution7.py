def find_min(nums):
    if len(nums) > 0 :
        min_num = nums[0]
        for i in nums:
            if i < min_num:
                min_num = i
            
        return min_num
    else:
        return None