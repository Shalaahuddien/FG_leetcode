class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = 2e9
        ans = 0
        for n in nums:
            mn = min(mn, n)
            ans = max(ans, n - mn)
        return ans if ans else -1
