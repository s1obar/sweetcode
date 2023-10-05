import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = collections.deque()    
    res = []

    l = r = 0

    while r < len(nums):
        # pop smaller values from the queue
        while dq and nums[dq[-1]] < nums[r]:
            dq.pop() 
        dq.append(r)

        # remove left value from vindow
        if l > dq[0]:
            dq.popleft()

        if (r + 1) >= k:
            res.append(nums[dq[0]])
            l += 1
        r += 1
    return res