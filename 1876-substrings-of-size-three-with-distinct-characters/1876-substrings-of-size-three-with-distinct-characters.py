class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if i + 2 < len(s):
                ss = s[i : i + 3]
                if len(set(ss)) == len(ss):
                    cnt += 1
        return cnt