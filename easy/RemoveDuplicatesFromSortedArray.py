from typing import List


def removeDuplicates(nums: List[int]):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
        
    print(nums)
    return j
            
        
    