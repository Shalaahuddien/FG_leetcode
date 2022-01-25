class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(K):
            res, l, r = 0, 0, 0
            o = 0
            while r < len(nums):
                c = nums[r]
                if c & 1: o += 1
                r += 1
                while o > K:
                    d = nums[l]
                    if d & 1: o -= 1
                    l += 1
                res += r - l + 1
            return res

        return atMost(k) - atMost(k - 1)