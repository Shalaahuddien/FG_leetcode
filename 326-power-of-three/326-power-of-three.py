class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(n):
            if n <= 1: return n == 1
            return n % 3 == 0 and rec(n // 3)

        return rec(n)