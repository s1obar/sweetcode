from typing import List

def removeElement(nums: List[int], val: int) -> int:
    for elem in reversed(nums):
        if elem == val:
            nums.pop(nums.index(elem))
    return len(nums)