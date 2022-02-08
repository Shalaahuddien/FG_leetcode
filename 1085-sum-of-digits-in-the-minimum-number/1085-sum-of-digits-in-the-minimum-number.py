class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        if sum(map(int, str(min(nums)))) % 2 == 1:
            return 0
        else:
            return 1
