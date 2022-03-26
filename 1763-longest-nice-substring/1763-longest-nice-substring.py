class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''
        for r in range(len(s)):
            for l in range(r):
                t = s[l:r+1]
                if set(t) == set(t.swapcase()):
                    ans = max(ans, t, key=len)
        return ans