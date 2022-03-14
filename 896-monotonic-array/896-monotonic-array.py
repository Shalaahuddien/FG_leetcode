class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            inc &= nums[i - 1] <= nums[i]
            dec &= nums[i - 1] >= nums[i]
        return inc or dec
