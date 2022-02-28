class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            ones += 1
            n &= (n-1)
        return ones