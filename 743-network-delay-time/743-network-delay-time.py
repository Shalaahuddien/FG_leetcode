class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 2e9
        dist = [0] + [INF]*n
        dist[k] = 0
        pq = [(0, k)]
        
        G = defaultdict(dict)
        for u,v,w in times:
            G[u][v] = w
            
        while pq:
            d,u = heappop(pq)
            if d > dist[u]:
                continue
            for v in G[u]:
                if d + G[u][v] < dist[v]:
                    dist[v] = d + G[u][v]
                    heappush(pq, (dist[v], v))
        if any(v == INF for v in dist):
            return -1
        return max(dist)