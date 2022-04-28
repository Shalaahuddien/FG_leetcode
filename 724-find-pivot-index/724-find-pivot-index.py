class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        tot = sum(nums)
        for i, n in enumerate(nums):
            right = tot - n - left
            if left == right:
                return i
            left += nums[i]
        return -1