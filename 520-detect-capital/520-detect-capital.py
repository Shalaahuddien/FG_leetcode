class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if word[0].isupper() and word[1:] == word[1:].lower():
            return True
        return False
        