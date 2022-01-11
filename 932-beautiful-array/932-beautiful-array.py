class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def rec(nums):
            if len(nums) <=2:
                return nums
            left = rec(nums[::2])
            right = rec(nums[1::2])
            return left+right
        return rec(list(range(1,n+1)))