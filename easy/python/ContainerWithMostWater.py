from typing import List

def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0

    while l < r: 
        area = (r - l) * min(height[r], height[l])
        res = max(area, res)

        if height[l] < height[r] or height[l] == height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
    return res