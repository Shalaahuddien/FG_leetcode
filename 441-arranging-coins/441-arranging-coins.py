class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n + 1
        while l < r:
            mid = (l + r) // 2
            if mid * (mid + 1) // 2 > n:
                r = mid
            else:
                l = mid + 1
        return l - 1