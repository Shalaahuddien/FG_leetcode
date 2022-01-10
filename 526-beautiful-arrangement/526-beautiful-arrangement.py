class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(bm, pl):
            if pl == 0:
                return 1
            S = 0
            for i in range(n):
                if not bm & 1 << i and ((i + 1) % pl == 0 or \
                     pl % (i + 1) == 0):
                    S += dfs(bm ^ 1 << i, pl - 1)
            return S

        return dfs(0, n)