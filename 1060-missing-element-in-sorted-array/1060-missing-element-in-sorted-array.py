class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n, n0 = len(nums), nums[0]
        # how many numbers are missing until nums[i]
        missing = lambda i: nums[i] - (n0 + i)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] - (n0 + m) >= k:
                r = m
            else:
                l = m + 1
        return nums[l - 1] + k - missing(l - 1)