class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        ALL = (1 << N) - 1
        cache = {}

        def dp(u, bm):
            state = (u, bm)
            if state in cache:
                return cache[state]
            if bm & (bm - 1) == 0:
                # Brian Kernighan method to check if num has only single bit set
                return 0
            cache[state] = float('inf')
            for v in graph[u]:
                if bm & (1 << v):  # cuz we are backward direction
                    already_visited = 1 + dp(v, bm)
                    not_visited = 1 + dp(v, bm ^ (1 << u))
                    cache[state] = min(cache[state], already_visited, not_visited)
            return cache[state]

        return min(dp(u, ALL) for u in range(N))