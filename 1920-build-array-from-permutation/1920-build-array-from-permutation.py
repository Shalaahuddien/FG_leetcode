class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i in range(len(nums)):
            r = nums[i]
            b = nums[nums[i]] % q
            nums[i] = b*q + r
            
        for i in range(len(nums)):
            nums[i] //= q
        return nums