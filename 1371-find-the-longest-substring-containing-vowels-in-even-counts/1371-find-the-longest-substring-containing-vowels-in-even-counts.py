class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {c:v for c,v in zip('aeiou', [0,1,2,3,4])}
        res = 0
        mask = 0
        occ = {0:-1}
        for i,c in enumerate(s):
            if c in d:
                mask ^= (1<<d[c])
            if mask!= 0 and mask not in occ:
                occ[mask] = i
            res = max(res, i-occ[mask])
        return res