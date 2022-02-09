class Solution:
    def minimumSum(self, num: int) -> int:
        A = sorted([int(c) for c in str(num)])
        return sum([A[0] * 10 + A[1] * 10 + A[2] + A[3]])
