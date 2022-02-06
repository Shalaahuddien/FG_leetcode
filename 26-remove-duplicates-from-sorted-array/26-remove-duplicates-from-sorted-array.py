class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        for n in nums:
            if w < 1 or n > nums[w-1]:
                nums[w] = n
                w += 1
        return w