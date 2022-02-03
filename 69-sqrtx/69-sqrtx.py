class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x
        while l < r:
            mid = (l + r) // 2
            # BUG: if mid**2 > x: eg. mid=2,x=4.
            if mid**2 > x:
                r = mid
            else:
                l = mid + 1

        return l - 1
