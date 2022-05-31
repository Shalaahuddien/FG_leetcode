class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre = {i: set() for i in range(1, n+1)}
        nxt = collections.defaultdict(set)
        for u, v in relations: 
            nxt[u].add(v)
            pre[v].add(u)
        queue = collections.deque([u for u in pre if not pre[u]])
        n -= len(queue)
        ans = 0
        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()
                for v in nxt[u]:
                    pre[v].remove(u)
                    if len(pre[v]) == 0:
                        queue.append(v)
                        n -= 1
            ans += 1
        return ans if n == 0 else -1