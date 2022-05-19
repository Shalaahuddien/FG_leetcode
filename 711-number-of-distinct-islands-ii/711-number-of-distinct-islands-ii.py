class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return
            grid[i][j] = 0
            path.append((i - row_ori, j - col_ori))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + dx, j + dy)

        def norm(path):
            rs, cs = zip(*path)  # Unzip path by calling zip(*path)
            rmin, cmin = min(rs), min(cs)
            return frozenset([(r - rmin, c - cmin) for r, c in path])

        unique_islands = set()
        for i in range(m):
            for j in range(n):
                path = []
                row_ori, col_ori = i, j
                dfs(i, j)
                if not path:
                    continue
                trans = []
                trans.append(norm([(+r, +c) for r, c in path]))
                trans.append(norm([(+r, -c) for r, c in path]))
                trans.append(norm([(-r, +c) for r, c in path]))
                trans.append(norm([(-r, -c) for r, c in path]))
                trans.append(norm([(+c, +r) for r, c in path]))
                trans.append(norm([(+c, -r) for r, c in path]))
                trans.append(norm([(-c, +r) for r, c in path]))
                trans.append(norm([(-c, -r) for r, c in path]))
                unique_islands.add(frozenset(trans))
        return len(unique_islands)