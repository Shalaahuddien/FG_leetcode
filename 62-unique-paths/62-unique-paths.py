class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DIR = [(0, 1), (1, 0)]

        @cache
        def dp(i, j):
            if (i, j) == (0, 0):
                return 1

            ans = 0
            for dx, dy in DIR:
                ii, jj = i - dx, j - dy
                if 0 <= ii < m and 0 <= jj < n:
                    ans += dp(ii, jj)
            return ans

        return dp(m - 1, n - 1)