class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        INF = 10**10
        dist = [[INF] * N for _ in range(N)]

        for u in range(N):
            dist[u][u] = 0
            for v in graph[u]:
                dist[u][v] = 1

        # Floyd-Warshall's ASSP
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        @cache
        def dp(node, visited):
            if visited == (1 << N) - 1:  # end_state
                return 0
            best = INF
            for i in range(N):
                if ((1 << i) & visited) == 0:  # unvisited i
                    best = min(best, dp(i, (1 << i) | visited) + dist[node][i])
            return best

        best = INF
        for i in range(N):
            best = min(best, dp(i, (1 << i)))
        return best