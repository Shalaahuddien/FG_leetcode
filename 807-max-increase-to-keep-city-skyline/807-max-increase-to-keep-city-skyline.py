class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mxr, mxc = {}, {}
        for r, row in enumerate(grid):
            mxr[r] = max(row)
        for c, col in enumerate(zip(*grid)):
            mxc[c] = max(col)
        gain = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                gain += min(mxr[r], mxc[c]) - grid[r][c]
        return gain
