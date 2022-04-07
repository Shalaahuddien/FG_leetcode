class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        l, winsm = 0,0
        for r in range(len(nums)):
            winsm += nums[r]
            while (r-l+1)*nums[r] - winsm > k:
                winsm -= nums[l]
                l += 1
            # max vallid window
            ans = max(ans, r-l+1)
        return ans