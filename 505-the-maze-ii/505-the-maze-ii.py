class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n, q = len(maze), len(maze[0]), [(0, start[0], start[1])]
        stopped = defaultdict(lambda: 1e6)
        stopped[(start[0], start[1])] = 0
        while q:
            dist, x, y = heapq.heappop(q)
            if dist > stopped[(x, y)]:
                continue
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                if dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1