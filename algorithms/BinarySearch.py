from typing import List

def binarySearch(nums: List[int], target: int) -> str:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return "Number {} has index {}".format(target, mid)
        elif target > nums[mid]:
            l = mid +1
        else:
            r = mid - 1