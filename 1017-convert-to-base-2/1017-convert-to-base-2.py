class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        res = []
        while n:
            res.append(n & 1)
            n = -(n>>1)
        return ''.join(map(str, res[::-1]))