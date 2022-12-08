class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)

        visited = [0] * n
        g = {x: set() for x in range(n)}
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)

        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1

        return ret