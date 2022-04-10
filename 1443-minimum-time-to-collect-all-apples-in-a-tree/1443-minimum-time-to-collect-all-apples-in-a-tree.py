class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        AL = defaultdict(list)
        for u, v in edges:
            AL[u].append(v)
            AL[v].append(u)

        def dfs(u):
            seen.add(u)
            appleInMe = hasApple[u]
            for v in AL[u]:
                if v in seen:
                    continue
                appleInMe |= dfs(v)
            if not appleInMe:
                del AL[u]
            return appleInMe
    
        seen = set()
        dfs(0)
        return max(0, 2 * (len(AL) - 1))