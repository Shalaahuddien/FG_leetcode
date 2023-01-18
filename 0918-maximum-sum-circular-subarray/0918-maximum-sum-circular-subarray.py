class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maximumSubArray(nums):
            ans = nums[0]
            sumSoFar = 0
            for num in nums:
                sumSoFar += num
                ans = max(ans, sumSoFar)
                if sumSoFar < 0:
                    sumSoFar = 0
            return ans

        def minimumSubArray(
            nums,
        ):  # the first element and the last element are exclusive!
            if len(nums) <= 2:
                return 0
            ans = nums[1]
            sumSoFar = 0
            for i in range(1, len(nums) - 1):
                sumSoFar += nums[i]
                ans = min(ans, sumSoFar)
                if sumSoFar > 0:
                    sumSoFar = 0
            return ans

        return max(maximumSubArray(nums), sum(nums) - minimumSubArray(nums))