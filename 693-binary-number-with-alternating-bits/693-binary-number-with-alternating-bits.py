class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = (n >> 1)
        last = n & 1
        while x:
            if last == x & 1:
                return False
            last = x & 1
            x >>= 1
        return True