class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        l = -1 if not left else max(left)
        r = n if not right else min(right)
        return max(l, n - r)