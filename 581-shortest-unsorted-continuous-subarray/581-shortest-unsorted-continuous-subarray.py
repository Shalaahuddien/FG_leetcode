class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        start, end = len(nums), 0
        for i, n in enumerate(nums):
            if n != snums[i]:
                start = min(i, start)
                end = max(i, end)
        return end - start + 1 if end - start >= 0 else 0