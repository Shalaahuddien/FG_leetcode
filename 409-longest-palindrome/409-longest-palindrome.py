class Solution:
    def longestPalindrome(self, s: str) -> int:
        C = Counter(s)
        ans = 0
        has_odds = 0
        for k, v in C.items():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
                has_odds += 1

        if has_odds:
            ans += 1
        return ans
