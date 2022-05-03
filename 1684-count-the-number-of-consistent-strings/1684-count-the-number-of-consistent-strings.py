class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = set(allowed)
        cnt = 0
        for w in words:
            for c in w:
                if c not in al:
                    cnt += 1
                    break
        return len(words) - cnt