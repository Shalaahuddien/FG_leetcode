class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
        i1 = l1 = 0
        i2 = l2 = 0
        while l1 < len(word1) or l2 < len(word2):
            if l1 == len(word1) or l2 == len(word2):
                return False
            if word1[l1][i1] != word2[l2][i2]:
                return False
            i1, i2 = i1 + 1, i2 + 1
            if i1 == len(word1[l1]):
                i1, l1 = 0, l1 + 1
            if i2 == len(word2[l2]):
                i2, l2 = 0, l2 + 1
        return True