class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dfs to find all cells in the current island
        def dfs(i, j, d):
            if not (0 <= i < m and 0 <= j < n):
                return
            if (i, j) in vis or not grid[i][j]:
                return
            vis.add((i, j))
            path_signature.append(d)
            dfs(i + 1, j, "D")
            dfs(i - 1, j, "U")
            dfs(i, j + 1, "R")
            dfs(i, j - 1, "L")
            path_signature.append("x")

        # repeatedly start DFS as long as there're islands remaining
        vis = set()
        unique_islands = set()
        for i in range(m):
            for j in range(n):
                path_signature = []
                dfs(i, j, "")
                if path_signature:
                    unique_islands.add("".join(path_signature))
        # print(unique_islands)
        return len(unique_islands)