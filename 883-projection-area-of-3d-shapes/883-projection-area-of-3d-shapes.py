class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        cnt = 0
        # xy:
        cnt += sum(1 for row in grid for r in row if r)
        # xz: <===
        cnt += sum(max(row) for row in grid)
        # yz: ^
        cnt += sum(max(col) for col in zip(*grid))
        return cnt