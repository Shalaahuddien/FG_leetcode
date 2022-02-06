class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r1 = r2 = w = 0
        while r2 < len(nums):
            r1 = r2
            dup = 0
            while r2 < len(nums) and nums[r1] == nums[r2]:
                r2 += 1
                dup += 1
                if dup <= 2:
                    nums[w] = nums[r1]
                    w += 1
        return w