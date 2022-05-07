class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = -2e9
        stk = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < k:
                return True
            while stk and stk[-1] < nums[i]:
                k = max(k, stk.pop())
            stk.append(nums[i])
        return False