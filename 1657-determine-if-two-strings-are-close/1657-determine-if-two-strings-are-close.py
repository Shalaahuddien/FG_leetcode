class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        C1, C2 = Counter(word1), Counter(word2)
        if sorted(C1.keys()) != sorted(C2.keys()):
            return False
        sv1, sv2 = sorted(C1.values()), sorted(C2.values())
        # print(sv1, sv2)
        if sv1 == sv2:
            return True
        for i in range(0, len(sv1), 3):
            if sv1[i:i + 3] != sv2[i:i + 3]:
                return False
        return True