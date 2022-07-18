class Solution:
    def numSubmatrixSumTarget(self, M: List[List[int]], target: int) -> int:
        m,n = len(M), len(M[0])
        for x in range(m):
            for y in range(n-1):
                M[x][y+1] += M[x][y]
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                s = 0
                presum = {0:1}
                for x in range(m):
                    s += M[x][y2] - (M[x][y1-1] if y1 > 0 else 0)
                    res += presum.get(s-target, 0)
                    presum[s] = presum.get(s, 0)+1
        return res