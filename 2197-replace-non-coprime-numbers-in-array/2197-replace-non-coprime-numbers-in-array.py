class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        def helper(A):
            stk = []
            for i in range(len(nums)):
                while stk and gcd(stk[-1], nums[i]) > 1:
                    nums[i] = lcm(stk.pop(), nums[i])
                stk.append(nums[i])
            return stk

        return helper(nums)