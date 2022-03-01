class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        for x in range(n+1):
            dp[x] = dp[x>>1] + (x&1)
        return dp