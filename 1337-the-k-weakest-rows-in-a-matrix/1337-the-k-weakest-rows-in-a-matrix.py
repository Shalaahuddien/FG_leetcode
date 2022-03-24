class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ones = []
        for i, row in enumerate(mat):
            ones.append((row.count(1), i))
        ones.sort()
        res = []
        for i in range(k):
            res.append(ones[i][1])
        return res
