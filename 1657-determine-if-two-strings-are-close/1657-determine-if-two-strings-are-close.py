class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        C1, C2 = Counter(word1), Counter(word2)
        return C1.keys() == C2.keys() \
            and Counter(C1.values()) == Counter(C2.values())