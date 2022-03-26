class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
            mn, mx = min(nums), max(nums)
            if mx - mn > 2 * k:
                return mx - mn - 2 * k
            return 0