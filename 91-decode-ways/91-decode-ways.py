class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s)-1:
                return 1
            ans = dfs(i+1)
            if int(s[i:i+2]) < 27:
                ans += dfs(i+2)
            return ans
        return dfs(0)