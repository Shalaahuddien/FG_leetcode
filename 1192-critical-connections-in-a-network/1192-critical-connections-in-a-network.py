class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.num = 0
        dfn = [None] * n
        low = [None] * n
        AL = defaultdict(list)
        for u, v in connections:
            AL[u].append(v)
            AL[v].append(u)
        res = []

        def dfs(u, par):
            if dfn[u] is not None:
                return
            dfn[u] = low[u] = self.num
            self.num += 1
            for v in AL[u]:
                if dfn[v] is None:
                    dfs(v, u)
            # minimal num in the neighbors except direct parent
            low[u] = min([dfn[u]] + [low[v] for v in AL[u] if v != par])

        dfs(0, None)
        for u, v in connections:
            # non bridge
            if low[u] > dfn[v] or low[v] > dfn[u]:
                res.append([u, v])
        return res