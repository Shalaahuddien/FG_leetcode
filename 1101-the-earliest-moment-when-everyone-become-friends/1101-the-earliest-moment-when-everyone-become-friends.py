class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda tu: tu[0])
        fa = {i: i for i in range(n)}
        groups = n

        def find(x) -> int:
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        for ts, x, y in logs:
            rx, ry = find(x), find(y)
            if rx != ry:
                fa[ry] = rx
                groups -= 1
                if groups == 1:
                    return ts
        return -1