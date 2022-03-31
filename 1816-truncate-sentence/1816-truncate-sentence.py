class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = 0
        for i in range(len(s)):
            if s[i] == " ":
                words += 1
            if words == k:
                return s[:i]
        return s