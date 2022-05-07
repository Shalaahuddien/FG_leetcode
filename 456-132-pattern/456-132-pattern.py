class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        leftMin = [float('inf')]*N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i-1], nums[i-1])
        stk =[]
        for j in range(N-1,-1,-1):
            numsk = float('-inf')
            while stk and stk[-1] < nums[j]:
                numsk= stk.pop()
            if leftMin[j] < numsk:
                return True
            stk.append(nums[j])
        return False
        