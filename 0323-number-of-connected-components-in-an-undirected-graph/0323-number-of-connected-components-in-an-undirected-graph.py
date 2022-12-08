class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {i: i for i in range(n)}

        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        for x, y in edges:
            fx, fy = find(x), find(y)
            if fx == fy:
                continue
            uf[fy] = fx

        return sum(i == f for i, f in uf.items())