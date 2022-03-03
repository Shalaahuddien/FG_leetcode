class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = [(-f, c) for c, f in Counter(s).items()]
        heapify(pq)
        mx_cnt = pq[0][0]
        if -mx_cnt > (len(s) + 1) // 2:
            return ""
        res = []
        while len(pq) >= 2:
            f0, c0 = heappop(pq)
            f1, c1 = heappop(pq)
            res.append(c0)
            res.append(c1)
            f0 += 1
            f1 += 1
            if -f0 > 0:
                heappush(pq, (f0, c0))
            if -f1 > 0:
                heappush(pq, (f1, c1))
        if pq:
            f, c = heappop(pq)
            res.append(c)
        return "".join(res)