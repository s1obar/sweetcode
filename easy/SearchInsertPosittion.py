from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if target < nums[i]:
                return nums.index(nums[i])
            elif target > nums[len(nums) - 1]:
                return len(nums)