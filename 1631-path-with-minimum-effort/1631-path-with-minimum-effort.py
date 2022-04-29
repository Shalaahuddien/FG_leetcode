class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = 2e9
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        dist = [[INF] * n for _ in range(m)]
        src, dst = (0, 0), (m - 1, n - 1)
        pq = [(0, src)]  # dist, row/col
        while pq:
            d, (r, c) = heappop(pq)
            if d > dist[r][c]:
                continue
            if (r, c) == dst:
                return d
            for i in range(4):
                xx, yy = r + DIR[i][0], c + DIR[i][1]
                if not (0 <= xx < m and 0 <= yy < n):
                    continue
                new_dist = max(d, abs(heights[xx][yy] - heights[r][c]))
                if dist[xx][yy] > new_dist:
                    dist[xx][yy] = new_dist
                    heappush(pq, (new_dist, (xx, yy)))