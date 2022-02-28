class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotting = {(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 2}
        fresh = {(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 1}
        ts = 0
        while fresh:
            if not rotting:
                return -1
            rotting = {(i + di, j + dj) for i, j in rotting for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (i + di, j + dj) in fresh}
            fresh -= rotting
            ts += 1
        return ts