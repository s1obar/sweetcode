from typing import List

def maxProduct(nums: List[int]) -> int:
    maxSub = max(nums)
    curMaxProduct = 1
    curMinProduct = 1

    for n in nums:
        tmp  = curMaxProduct * n
        curMaxProduct = max(tmp, n * curMinProduct, n)
        curMinProduct = min(tmp, n * curMinProduct, n)
        maxSub = max(maxSub, curMaxProduct)
    return maxSub