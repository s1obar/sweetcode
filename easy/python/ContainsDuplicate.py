from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    for i,n in enumerate(nums):
        if n in hashset:
            return True
        hashset.add(n)
    return False