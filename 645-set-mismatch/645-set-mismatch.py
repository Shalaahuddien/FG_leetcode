class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tot = (1 + n) * n // 2
        dup = sum(nums) - sum(set(nums))
        miss = tot - sum(set(nums))
        return [dup, miss]