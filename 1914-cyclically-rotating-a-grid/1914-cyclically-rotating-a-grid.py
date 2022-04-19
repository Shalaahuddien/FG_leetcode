class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        T, L = 0, 0
        B, R = m - 1, n - 1

        while T < B and L < R:
            no_elems = 2 * (B - T + 1) + 2 * (R - L + 1) - 4
            no_rotate = k % no_elems
            for _ in range(no_rotate):
                tmp = grid[T][L]
                for j in range(L, R):
                    grid[T][j] = grid[T][j + 1]
                for i in range(T, B):
                    grid[i][R] = grid[i + 1][R]
                for j in range(R, L, -1):
                    grid[B][j] = grid[B][j - 1]
                for i in range(B, T, -1):
                    grid[i][L] = grid[i - 1][L]
                grid[T + 1][L] = tmp
            T, L = T + 1, L + 1
            B, R = B - 1, R - 1
        return grid