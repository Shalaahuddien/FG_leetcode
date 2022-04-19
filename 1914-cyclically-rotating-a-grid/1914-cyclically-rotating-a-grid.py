class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        T, L = 0, 0
        B, R = m - 1, n - 1
        while T < B and L < R:
            path = []
            for c in range(L, R):
                path.append(grid[T][c])
            for r in range(T, B):
                path.append(grid[r][R])
            for c in range(R, L, -1):
                path.append(grid[B][c])
            for r in range(B, T, -1):
                path.append(grid[r][L])

            kk = k % len(path)
            path = path[kk:] + path[:kk]
            i = 0
            for c in range(L, R):
                grid[T][c] = path[i]
                i += 1
            for r in range(T, B):
                grid[r][R] = path[i]
                i += 1
            for c in range(R, L, -1):
                grid[B][c] = path[i]
                i += 1
            for r in range(B, T, -1):
                grid[r][L] = path[i]
                i += 1
            T, L = T + 1, L + 1
            B, R = B - 1, R - 1

        return grid