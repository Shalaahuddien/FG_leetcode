class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l,r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l,r = l-1,r+1
                cnt += 1
            return cnt
        
        ans = 0
        n = len(s)
        for i in range(len(s)):
            ans += expand(i,i)
            ans += expand(i,i+1)
        return ans