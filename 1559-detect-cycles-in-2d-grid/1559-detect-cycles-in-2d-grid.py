class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(v, fa):
            if v in seen:
                return True
            seen.add(v)
            x, y = v
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                # !no back edge (u->v->w), so don't choose u === w.
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == grid[x][y] and (xx, yy) != fa:
                    w = (xx, yy)
                    if dfs(w, v):
                        return True
            return False

        seen = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) in seen:
                    continue
                if dfs((i, j), None):
                    return True
        return False