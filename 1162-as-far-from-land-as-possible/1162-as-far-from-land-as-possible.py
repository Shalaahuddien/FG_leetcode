class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m * n:
            return -1
        seen = set(q)
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0 and (xx, yy) not in seen:
                        q.append((xx, yy))
                        seen.add((xx, yy))
            step += 1

        return step - 1