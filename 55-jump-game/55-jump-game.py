class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dp(i):
            if i == len(nums)-1:
                return True
            if any(dp(j) for j in range(i+1, min(i+nums[i]+1, len(nums)))[::-1]):
                return True
            return False
        return dp(0)