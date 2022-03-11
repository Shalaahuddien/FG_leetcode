class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum([freq % 2 for _, freq in Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1