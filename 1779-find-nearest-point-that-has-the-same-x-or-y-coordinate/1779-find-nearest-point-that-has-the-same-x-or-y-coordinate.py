class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx, mn = -1, 2e9
        for i, (r, c) in enumerate(points):
            dx, dy = x - r, y - c
            # at least one of them is zero, so take advantage of that.
            if dx * dy == 0 and abs(dx + dy) < mn:
                mn = abs(dx + dy)
                idx = i
        return idx
