class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        class UF:
            def __init__(self, n) -> None:
                self.pa = list(range(n))
                self.sz = [1] * n
                self.cnt = n

            def find(self, i):
                if self.pa[i] != i:
                    self.pa[i] = self.find(self.pa[i])
                return self.pa[i]

            def union(self, x, y):
                if x == y:
                    return
                if self.sz[x] > self.sz[y]:
                    x, y = y, x
                self.pa[x] = y
                self.sz[y] += self.sz[x]
                self.cnt -= 1

            def find_and_union(self, i, j):
                # T: not connected, but cycle after union! F: already same group
                x, y = map(self.find, [i, j])
                if x == y:
                    return False
                self.union(x, y)
                return True

        m, n = len(grid), len(grid[0])
        uf = UF(m * n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.find_and_union((i * n+j), ((i - 1) * n + j)):
                        return True

                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.find_and_union((i * n + j), (i * n + j - 1)):
                        return True
        return False