class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([(start, 0)])
        vis = set(q)

        while q:
            for _ in range(len(q)):
                v, s = q.popleft()
                if v == goal:
                    return s
                if s == 1000:
                    return -1
                if not (0 <= v <= 1000):
                    continue
                for n in nums:
                    if v + n not in vis:
                        q.append((v + n, s + 1))
                        vis.add(v + n)
                    if v - n not in vis:
                        q.append((v - n, s + 1))
                        vis.add(v - n)
                    if v ^ n not in vis:
                        q.append((v ^ n, s + 1))
                        vis.add(v ^ n)
        return -1