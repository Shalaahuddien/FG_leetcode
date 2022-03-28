class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l, r = l + 1, r - 1
        if l >= r:
            return 1
        return 2
