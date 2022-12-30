class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res