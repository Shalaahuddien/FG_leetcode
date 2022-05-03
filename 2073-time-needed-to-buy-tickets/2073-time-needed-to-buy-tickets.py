class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([[t, i] for i, t in enumerate(tickets)])
        sec = 0
        while q:
            t, i = q.popleft()
            if i == k and t == 1:
                return sec + 1
            q.append([t - 1 if t > 0 else 0, i])
            if t != 0:
                sec += 1