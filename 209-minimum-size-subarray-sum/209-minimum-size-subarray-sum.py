class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,n = 0,0,len(nums)
        ans = n+1
        wind = 0
        while r < n:
            wind += nums[r]
            r += 1
            while wind >= target:
                ans = min(ans, r-l)
                wind -= nums[l]
                l += 1
        return ans if ans != n+1 else 0
                