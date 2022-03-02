class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = [(-f, c) for c, f in Counter(s).items()]
        heapify(pq)

        res = []
        while len(pq) >= 2:
            f0, c0 = heappop(pq)
            f1, c1 = heappop(pq)
            res.append(c0)
            res.append(c1)
            if -f0 - 1 > 0:
                heappush(pq, (f0 + 1, c0))
            if -f1 - 1 > 0:
                heappush(pq, (f1 + 1, c1))
        if pq:
            f, c = heappop(pq)
            if -f > 1:
                return ""
            res.extend([c] * (-f))
        return "".join(res)