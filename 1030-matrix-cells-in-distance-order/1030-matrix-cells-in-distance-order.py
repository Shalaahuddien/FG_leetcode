class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = set()
        for d in range(rows - 1 + cols - 1 + 1):
            for dx in range(d + 1):
                dy = d - dx
                for sx, sy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    nx, ny = rCenter + sx * dx, cCenter + sy * dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        res.add((nx, ny))
        sres = list(res)
        sres.sort(key=lambda x: (abs(x[0] - rCenter) + abs(x[1] - cCenter)))
        return sres
        return list(res)