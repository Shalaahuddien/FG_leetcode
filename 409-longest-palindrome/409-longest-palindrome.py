class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum([freq % 2 for freq in Counter(s).values()])
        return len(s) if odds <= 1 else len(s) - odds + 1