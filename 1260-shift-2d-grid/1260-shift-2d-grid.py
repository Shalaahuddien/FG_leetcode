class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m * n

        start_idx, count = 0, 0
        while count < (m * n):
            cur_idx, pre_v = start_idx, grid[start_idx // n][start_idx % n]
            while True:
                nxt_idx = (cur_idx + k) % (m * n)
                i, j = divmod(nxt_idx, n)
                grid[i][j], pre_v = pre_v, grid[i][j]
                cur_idx = nxt_idx
                count += 1
                if cur_idx == start_idx:
                    break
            start_idx += 1
        return grid