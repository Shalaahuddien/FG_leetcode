class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left = 0
        for i, n in enumerate(nums):
            right = tot - n - left
            if left == right:
                return i
            left += n
        return -1