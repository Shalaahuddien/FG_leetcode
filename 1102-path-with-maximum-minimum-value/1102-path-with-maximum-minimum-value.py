class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        root = list(range(R * C))
        sz = [1] * (R * C)
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            x, y = map(find, [i, j])
            if x == y:
                return
            if sz[x] > sz[y]:
                x, y = y, x
            # make sure px is smaller coorp
            root[x] = y
            sz[y] += sz[x]

        vals = [(r, c) for r in range(R) for c in range(C)]
        vals.sort(key=lambda x: grid[x[0]][x[1]], reverse=True)
        for i, j in vals:
            visited.add((i, j))
            for di, dj in D:
                ii, jj = i + di, j + dj
                if 0 <= ii < R and 0 <= jj < C and (ii, jj) in visited:
                    # XXX: only union if cur and neighbor are visited
                    p, pp = i * C + j, ii * C + jj
                    union(p, pp)
                    # check if top-left is connected w/ bottom-right
                    if find(0) == find(R * C - 1):
                        return grid[i][j]
        return -1