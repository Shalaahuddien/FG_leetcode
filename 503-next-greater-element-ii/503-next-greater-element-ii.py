class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        n = len(nums)
        ans = [-1] * n
        for ci in range(n * 2 - 1, -1, -1):
            i = ci % n
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            ans[i] = nums[stk[-1]] if stk else -1
            stk.append(i)
        return ans