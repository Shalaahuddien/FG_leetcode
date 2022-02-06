class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        for n in nums:
            if w < 2 or n > nums[w-2]:
                nums[w] = n
                w += 1
        return w