class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums) // 2]
        res = sum(abs(med - n) for n in nums)
        return res