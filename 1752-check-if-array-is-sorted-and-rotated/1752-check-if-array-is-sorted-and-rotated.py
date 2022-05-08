class Solution:
    def check(self, nums: List[int]) -> bool:
        mn = nums[0]
        for i in range(len(nums) - 1):
            if not nums[i] <= nums[i + 1]:
                break
        else:
            return True
        for j in range(i + 1, len(nums)):
            if nums[j] > mn or j + 1 < len(nums) and nums[j] > nums[j + 1]:
                return False
        return True