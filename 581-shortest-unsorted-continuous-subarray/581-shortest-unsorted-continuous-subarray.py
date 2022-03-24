class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stk = []
        l, r = len(nums), 0
        for i, n in enumerate(nums):
            while stk and nums[stk[-1]] > n:
                l = min(stk.pop(), l)
            stk.append(i)
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                r = max(stk.pop(), r)
            stk.append(i)
        return r - l + 1 if r - l > 0 else 0