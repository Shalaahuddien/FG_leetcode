class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def dfs(i, j):
            vis.add((i, j))
            res.append((i, j))
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in vis:
                    dfs(x, y)
        res, vis = [], set()
        dfs(rCenter, cCenter)
        res.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return res