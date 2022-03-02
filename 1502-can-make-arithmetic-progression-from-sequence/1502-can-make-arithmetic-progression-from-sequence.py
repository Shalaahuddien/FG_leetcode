class Solution:
    def canMakeArithmeticProgression(self, A: List[int]) -> bool:
        gap = (max(A) - min(A)) / (len(A) - 1)
        if gap == 0:
            return True
        s = set(n - min(A) for n in A)
        return len(s) == len(A) and all(diff % gap == 0 for diff in s)