class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        ans = 0
        zeros = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            if c == 0:
                zeros += 1
            while zeros > k:
                d = nums[l]
                l += 1
                if d == 0:
                    zeros -= 1
            # now windows at most k flip
            ans = max(ans, r - l)
        return ans