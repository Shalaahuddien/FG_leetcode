class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            x = nums[i]
            if x < n and x != i:
                nums[i],nums[x] = nums[x], nums[i]
            else:
                i += 1
        for i,x in enumerate(nums):
            if i != x:
                return i
        return n