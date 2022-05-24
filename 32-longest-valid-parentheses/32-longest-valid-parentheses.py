class Solution:
    def longestValidParentheses(self, s: str) -> int:
        @cache
        def dp(i):
            if i < 0 or s[i] == "(":
                return 0
            j = i - dp(i - 1) - 1
            if j >= 0 and s[j] == "(":
                return 2 + dp(i - 1) + dp(j - 1)
            return 0

        return max(dp(i) for i in range(len(s))) if s else 0
