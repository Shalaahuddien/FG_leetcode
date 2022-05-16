class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == "0":
                return 0
            grid[i][j] = "0"
            for dx, dy in DIR:
                dfs(i + dx, j + dy)
            return 1

        cc = 0
        for i in range(m):
            for j in range(n):
                cc += dfs(i, j)
        return cc