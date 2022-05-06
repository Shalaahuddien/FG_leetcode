class Solution:
    def findPermutation(self, s: str) -> List[int]:
        AL = defaultdict(list)
        ins = [0 for i in range(len(s) + 1)]
        for i, c in enumerate(s):
            if c == "I":
                AL[i].append(i + 1)
                ins[i + 1] += 1
            else:
                AL[i + 1].append(i)
                ins[i] += 1
        pq = [i for i in range(len(s) + 1) if ins[i] == 0]
        heapify(pq)

        # topo_ord = []
        ele = 1
        res = [0] * (len(s) + 1)
        while pq:
            u = heappop(pq)
            # topo_ord.append(ele)
            res[u] = ele
            ele += 1
            for v in AL[u]:
                ins[v] -= 1
                if ins[v] == 0:
                    heappush(pq, v)
        return res