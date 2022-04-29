class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(heights), len(heights[0])

        def dfs(LIMIT, i, j):
            vis.add((i, j))
            for dx, dy in DIR:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in vis:
                    if abs(heights[i][j] - heights[x][y]) <= LIMIT:
                        dfs(LIMIT, x, y)

        l, r = 0, max(max(heights, key=max))
        while l < r:
            mid = (l + r) // 2
            vis = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in vis:
                r = mid
            else:
                l = mid + 1
        return l