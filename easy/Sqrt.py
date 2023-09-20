import math

def mySqrt(x: int) -> int:
    left, right = 0, x
    result = 0

    while left <= right:
        mid = left + ((right - left) // 2) # this will never overflow, m = left + right // 2 -> this can overflow, better use equasion below

        if mid**2 > x:
            right = mid - 1
        elif mid**2 < x:
            left = mid + 1
            result = mid
        else:
            return mid
    return result
