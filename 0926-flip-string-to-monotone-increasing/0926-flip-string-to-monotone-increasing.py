class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        s = [int(i) for i in s] + [1]
        
        @cache
        def dp(i, k):
            if i == -1: return 0
            return min([dp(i-1, j) + int(k != s[i]) for j in range(k + 1)])
           
        return dp(len(s) - 1, 1)