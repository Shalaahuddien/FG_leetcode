class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < nums[0]:
            return len(nums)

        for x in range(nums[0], nums[-1] + 1):
            ge_x = len(nums) - bisect_left(nums, x)
            if ge_x == x:
                return x
        return -1