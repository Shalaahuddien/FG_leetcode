class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ''
        n = len(s)

        def cent_expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l-1, r+1
            return r-l-1

        start, end = 0, 0
        for c in range(n):
            l_even = cent_expand(c, c)
            l_odd = cent_expand(c, c+1)
            mx = max(l_even, l_odd)
            if mx > end-start+1:
                start = c - (mx-1)//2
                end = c + mx//2
        return s[start:end+1]
