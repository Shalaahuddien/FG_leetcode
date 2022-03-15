class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AL = defaultdict(list)
        DEG = {u: 0 for u in range(numCourses)}
        for c, p in prerequisites:
            AL[p].append(c)
            DEG[c] += 1
        m = numCourses
        q = deque([i for i in range(m) if DEG[i] == 0])
        ts = []
        while q:
            u = q.popleft()
            ts.append(u)
            if len(ts) == m:
                return ts
            for v in AL[u]:
                DEG[v] -= 1
                if DEG[v] == 0:
                    q.append(v)
        return []