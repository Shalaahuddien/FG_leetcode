class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bad = set(brokenLetters)
        return len([w for w in text.split() if not set(w).intersection(bad)])
