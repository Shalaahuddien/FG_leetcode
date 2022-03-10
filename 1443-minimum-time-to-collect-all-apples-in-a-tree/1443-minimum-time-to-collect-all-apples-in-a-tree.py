class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        AL = defaultdict(list)
        for x, y in edges:
            AL[x].append(y)
            AL[y].append(x)

        def dfs(u) -> bool:
            seen.add(u)
            res = hasApple[u]
            for v in AL[u]:
                if v not in seen:
                    res |= dfs(v)
            if res:
                VALID.add(u)
            return res

        VALID = set()
        seen = set()
        dfs(0)
        return max(0, 2 * (len(VALID) - 1))