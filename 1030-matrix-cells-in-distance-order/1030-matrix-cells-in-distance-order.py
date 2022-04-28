class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        q, res = deque([(rCenter, cCenter)]), []
        vis = set(q)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                res.append((r, c))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    xx, yy = r + dx, c + dy
                    if 0 <= xx < rows and 0 <= yy < cols and (xx, yy) not in vis:
                        vis.add((xx, yy))
                        q.append((xx, yy))
        return res