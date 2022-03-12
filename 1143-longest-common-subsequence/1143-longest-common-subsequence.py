class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(s1) or j == len(s2):
                return 0
            elif s1[i] == s2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)