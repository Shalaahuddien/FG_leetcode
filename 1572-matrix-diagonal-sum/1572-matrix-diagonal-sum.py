class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        ans = 0
        for i in range(N):
            ans += mat[i][i]
            ans += mat[N - 1 - i][i]
        if N % 2 == 1:
            ans -= mat[N // 2][N // 2]
        return ans