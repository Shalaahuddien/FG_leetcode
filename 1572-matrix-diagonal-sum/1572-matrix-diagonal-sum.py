class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        ans = 0
        for r in range(N):
            for c in range(N):
                if r == c:
                    ans += mat[r][c]
                if r + c == N - 1:
                    ans += mat[r][c]
        if N % 2 == 1:
            ans -= mat[N // 2][N // 2]
        return ans
