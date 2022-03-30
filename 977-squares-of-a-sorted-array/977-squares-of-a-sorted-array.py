class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            left, right = nums[l], nums[r]
            if abs(left) > abs(right):
                res[i] = left * left
                l += 1
            else:
                res[i] = right * right
                r -= 1
        return res