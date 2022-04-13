class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 0, 1
        for i in range(n * n):
            M[x][y] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or M[x + dx][y + dy] != 0:
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        return M