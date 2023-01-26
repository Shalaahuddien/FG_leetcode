class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        AL = defaultdict(dict)
        for s, d, w in flights:
            AL[s][d] = w
        pq = [(0, src, k + 1)]  # (dist, node, stops)
        vis = [0] * n
        while pq:
            w, x, lk = heappop(pq)
            if x == dst:
                return w
            if vis[x] >= lk:
                continue
            vis[x] = lk
            for y, dw in AL[x].items():
                heappush(pq, (w + dw, y, lk - 1))
        return -1