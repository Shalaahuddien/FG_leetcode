class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = set(allowed)
            # res = []
        cnt = 0
        for w in words:
            if set(w) <= al:
                cnt += 1
        return cnt