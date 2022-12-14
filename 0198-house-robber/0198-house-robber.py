class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def fn(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + fn(i+2), fn(i+1))
        return fn(0)