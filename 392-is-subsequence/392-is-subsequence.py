class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)

        @cache
        def dp(i, j):
            if i == slen:
                return True
            if j == tlen:
                return False
            if s[i] == t[j]:
                return dp(i + 1, j + 1)
            else:
                return dp(i, j + 1)
                # return dp(i + 1, j) or dp(i, j + 1)

        return dp(0, 0)