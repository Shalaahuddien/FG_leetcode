class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        vi = {0: -1}
        P = 0
        mx = 0
        for i, v in enumerate(nums):
            P += v if v == 1 else -1
            if P in vi:
                mx = max(mx, i - vi[P])
            else:
                vi[P] = i
        return mx