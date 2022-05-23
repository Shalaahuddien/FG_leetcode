class Solution:
    def numSquares(self, n: int) -> int:
        evens = [i**2 for i in range(100, 0, -1)]

        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            return min([dp(i - e) + 1 for e in evens if i >= e])

        return dp(n)