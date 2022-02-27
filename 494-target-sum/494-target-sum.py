class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, s) -> int:
            # base case
            if i == len(nums):
                if s == 0:
                    return 1
                return 0

            # DP formula
            return dp(i + 1, s - nums[i]) + dp(i + 1, s + nums[i])

        # driver code
        if not nums:
            return 0
        return dp(0, target)