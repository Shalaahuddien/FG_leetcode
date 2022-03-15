class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        f = lambda c: ord(c)-ord('a')
        n,h,d,m = len(needle), len(haystack), ord('z')-ord('a')+1, sys.maxsize
        if n > h: return -1
        nd, hash_n, hash_h = d**(n-1),0,0
        # init hash
        for i in range(n):
            hash_n = (d*hash_n + f(needle[i])) % m
            hash_h = (d*hash_h + f(haystack[i])) % m
        if hash_n == hash_h: return 0
        for i in range(1, h-n+1):
            hash_h = (d* (hash_h - f(haystack[i-1])*nd) + f(haystack[i+n-1])) % m
            if hash_n == hash_h:
                return i
        return -1