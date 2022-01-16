class Solution:
    def findNthDigit(self, n: int) -> int:
        start, bit, cnt = 1, 1, 9
        while n - bit*cnt>0:
            n -= bit*cnt
            bit += 1
            cnt *= 10
            start*=10
            
        d,m = divmod(n-1, bit)
        return str(start + d)[m]