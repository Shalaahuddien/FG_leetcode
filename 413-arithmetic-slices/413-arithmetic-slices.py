class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        @cache
        def arith(i):
            """
            # of arithmetic slices in prefix nums[0...i]
            """
            if i < 2:
                return 0
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                return 1 + arith(i - 1)
            else:
                return 0

        return sum(arith(i) for i in range(2, len(nums)))