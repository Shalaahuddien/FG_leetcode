class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            lr = nums[l] + nums[r]
            if lr < k:
                l += 1
            elif lr > k:
                r -= 1
            else:
                res += 1
                l, r = l + 1, r - 1
        return res