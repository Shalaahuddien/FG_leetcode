class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AL = defaultdict(list)
        #! must use Dictionary Comprehension, rather defaultdict
        DEG = {v: 0 for v in range(numCourses)}
        for a, b in prerequisites:
            AL[b].append(a)
            DEG[a] += 1

        q = deque([v for v in DEG if DEG[v] == 0])
        ts = []
        while q:
            u = q.popleft()
            ts.append(u)
            if len(ts) == numCourses:
                return True
            for v in AL[u]:
                DEG[v] -= 1
                if DEG[v] == 0:
                    q.append(v)
        return False