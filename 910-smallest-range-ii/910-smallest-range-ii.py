class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = nums[0] + k, nums[-1] - k
        ans = nums[-1] - nums[0]
        for p in range(len(nums) - 1):
            mn, mx = min(nums[p + 1] - k, left), max(nums[p] + k, right)
            ans = min(mx - mn, ans)
        return ans