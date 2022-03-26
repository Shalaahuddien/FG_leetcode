class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
            mn, mx = min(nums), max(nums)
            return max(0, mx - mn - 2 * k)