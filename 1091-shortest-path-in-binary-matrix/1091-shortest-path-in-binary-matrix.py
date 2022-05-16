class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        R, C = len(grid), len(grid[0])

        src, dst = (0, 0), (R - 1, C - 1)
        q = deque([src])
        if grid[0][0] == 1:
            return -1
        grid[0][0] = 1
        step = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                # process cur
                if (i, j) == dst:
                    return step
                for dx, dy in DIR:
                    x, y = i + dx, j + dy
                    if not (0 <= x < R and 0 <= y < C and grid[x][y] == 0):
                        continue
                    grid[x][y] = 1
                    q.append((x, y))
            step += 1
        return -1