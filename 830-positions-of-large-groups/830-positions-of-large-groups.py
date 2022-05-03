class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l, r = 0, 0
        res = []
        while l < len(s):
            while r < len(s) and s[l] == s[r]:
                r += 1
            # r == len(s) or s[l] != s[r]:
            if r - l >= 3:
                res.append([l, r - 1])
            l = r
        return res