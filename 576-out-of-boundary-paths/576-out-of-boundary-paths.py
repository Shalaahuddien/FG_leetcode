class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        @cache
        def dp(i,j,left):
            if not (0<=i<m and 0<=j<n):
                return 1
            if left == 0:
                return 0
            res = 0
            for dx,dy in DIR:
                res += dp(i+dx,j+dy,left-1) 
            return res% 1_000_000_007
        return dp(startRow, startColumn, maxMove)