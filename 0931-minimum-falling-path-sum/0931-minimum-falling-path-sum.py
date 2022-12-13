class Solution:
    def minFallingPathSum(self, M: List[List[int]]) -> int:
        @cache
        def fn(y, x):
            return min((M[y][x] + fn(y + 1, i) for i in range(x - 1, x + 2) if y + 1 < len(M) and 0 <= i < len(M[0])), default=M[y][x])

        return min(fn(0, x) for x in range(len(M[0])))