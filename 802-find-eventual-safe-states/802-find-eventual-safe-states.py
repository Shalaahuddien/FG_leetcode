class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        W, G, B = 0, 1, 2
        colr = defaultdict(int)

        def dfs(u):
            if colr[u] != W:
                return colr[u] == B

            colr[u] = G
            for v in graph[u]:
                if colr[v] == B:
                    continue
                if colr[v] == G or not dfs(v):
                    return False
            colr[u] = B
            return True

        return list(filter(dfs, range(len(graph))))