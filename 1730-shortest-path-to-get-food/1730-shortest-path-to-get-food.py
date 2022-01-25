class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        steps = 0
        q = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i, j))
                    visited.add((i,j))
                    break

        while q:
            qlen = len(q)
            for _ in range(qlen):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and (xx,yy) not in visited:
                        if grid[xx][yy] == '#':
                            return steps + 1
                        elif grid[xx][yy] == 'O':
                            q.append((xx, yy))
                            visited.add((xx,yy))
            steps += 1
        return -1