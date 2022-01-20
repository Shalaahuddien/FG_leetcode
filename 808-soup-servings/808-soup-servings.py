class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dp(a, b):
            if a <= 0 and b > 0: return 1
            elif a <= 0 and b <= 0: return 0.5
            elif a > 0 and b <= 0: return 0
            return 0.25*(dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) \
                + dp(a-1,b-3))

        if n > 5000: return 1
        n = ceil(n / 25)
        return dp(n, n)