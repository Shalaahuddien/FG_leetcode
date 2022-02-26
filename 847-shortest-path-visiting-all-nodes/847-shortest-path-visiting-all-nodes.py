class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        ALL = (1 << n) - 1
        q = deque([(u, 1 << u) for u in range(n)])
        seen = set(q)
        steps = 0
        while q:
            for _ in range(len(q)):
                u, bm = q.popleft()
                for v in graph[u]:
                    v_bm = bm | (1 << v)
                    if v_bm == ALL:
                        return 1 + steps
                    if (v, v_bm) not in seen:
                        seen.add((v, v_bm))
                        q.append((v, v_bm))
            steps += 1
        return -1  # no way to reach here