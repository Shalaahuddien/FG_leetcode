class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dp(n, i):
            if n == 0: return 1  # Found a valid answer
            if i == 5:  return 0  # Reach to length of vowels [a, e, i, o, u]
            ans = dp(n, i + 1)  # Skip vowels[i]
            ans += dp(n - 1, i)  # Include vowels[i]
            return ans

        return dp(n, 0)