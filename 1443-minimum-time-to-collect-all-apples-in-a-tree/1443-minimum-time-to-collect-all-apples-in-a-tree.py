class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        AL = defaultdict(list)
        for u, v in edges:
            AL[u].append(v)
            AL[v].append(u)

        # @cache
        def dfs(u):
            seen.add(u)
            selfOfKidHasApple = hasApple[u]
            for v in AL[u]:
                if v not in seen:
                    selfOfKidHasApple |= dfs(v)
            if not selfOfKidHasApple:
                AL.pop(u)
            return selfOfKidHasApple
    
        seen = set()
        dfs(0)
        return max(0, 2 * (len(AL) - 1))