class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m = {}
            for w, p in zip(word, pattern):
                if m.setdefault(w, p) != p:
                    return False
            return len(set(m.values())) == len(m.values())

        return list(filter(match, words))
