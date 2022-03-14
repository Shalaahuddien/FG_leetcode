class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            if s[i] == s[j]:
                return dp(i + 1, j - 1) + 2
            else:
                return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, len(s) - 1) >= len(s) - k
