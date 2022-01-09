class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        n = len(nums)
        res = n
        cnt = 0
        l, r = 0, 0
        while r < 2 * n:
            c = nums[r % n]
            r += 1
            cnt += c
            while r - l >= ones:
                d = nums[l % n]
                l += 1
                res = min(res, ones - cnt)
                cnt -= d
        return res