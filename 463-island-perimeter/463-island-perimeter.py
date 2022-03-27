class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, p = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                p += 4 * grid[i][j]
                if i > 0:
                    p -= grid[i][j] * grid[i - 1][j]
                if i + 1 < m:
                    p -= grid[i][j] * grid[i + 1][j]
                if j > 0:
                    p -= grid[i][j] * grid[i][j - 1]
                if j + 1 < n:
                    p -= grid[i][j] * grid[i][j + 1]
        return p