class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(u)->bool:
            for v in graph[u]:
                if v in color:
                    if color[v] == color[u]:
                        return False
                else:
                    color[v] = 1-color[u]
                    if not dfs(v):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True