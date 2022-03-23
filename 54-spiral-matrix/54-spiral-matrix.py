class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        dx, dy = DIR[0]
        di = 0
        ans = []
        for _ in range(m * n):
            if not 0 <= x + dx < m or not 0 <= y + dy < n or matrix[x + dx][y + dy] == "*":
                di = (di + 1) % 4
                dx, dy = DIR[di]
            ans.append(matrix[x][y])
            matrix[x][y] = "*"
            x, y = x + dx, y + dy
        return ans