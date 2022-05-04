class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mn, mx = nums[-1], nums[0]
        begin, end = 0, -1
        for i in range(len(nums)):
            if nums[i] < mx:
                end = i
            else:
                mx = nums[i]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > mn:
                begin = i
            else:
                mn = nums[i]
        return end - begin + 1