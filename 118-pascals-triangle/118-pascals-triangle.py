class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for r in range(1, numRows):
            next = []
            pre = [0] + res[-1] + [0]
            for i in range(len(pre)-1):
                next.append(pre[i]+pre[i+1])
            res.append(next)
        return res