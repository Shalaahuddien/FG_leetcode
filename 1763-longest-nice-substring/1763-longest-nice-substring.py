class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dc(s):
            if len(s) < 2: return ''
            ss = set(s)
            for i,c in enumerate(s):
                if c.swapcase() not in ss:
                    nl = dc(s[:i])
                    nr = dc(s[i+1:])
                    return max(nl,nr,key=len)
            return s
        return dc(s)