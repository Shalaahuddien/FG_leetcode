class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        cnt = 0
        l, r = 0, 0
        p = 1
        while r < len(nums):
            c = nums[r]
            r += 1
            p *= c
            while l < r and p >= k:
                d = nums[l]
                l += 1
                p //= d
            # now p < k
            cnt += r - l

        return cnt