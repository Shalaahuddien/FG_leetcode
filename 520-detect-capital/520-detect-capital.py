class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        cnt = sum(c.isupper() for c in word)
        return cnt == len(word) \
            or cnt == 0 \
                or cnt == 1 and word[0].isupper()