class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([0])
        vis = set(q)
        coins.sort()
        step = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if u == amount:
                    return step
                for c in coins:
                    v = u + c
                    if v in vis:
                        continue
                    if v > amount:
                        break
                    vis.add(v)
                    q.append(v)
            step += 1
        return -1