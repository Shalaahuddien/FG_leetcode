class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(row, col1, col2):
            if not (0 <= col1 < n and 0 <= col2 < n):
                return -1000_000
            # current cell
            result = 0
            result += grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            # transition
            if row != m - 1:
                result += max(
                    dp(row + 1, new_col1, new_col2)
                    for new_col1 in [col1, col1 + 1, col1 - 1]
                    for new_col2 in [col2, col2 + 1, col2 - 1]
                )
            return result

        return dp(0, 0, n - 1)

