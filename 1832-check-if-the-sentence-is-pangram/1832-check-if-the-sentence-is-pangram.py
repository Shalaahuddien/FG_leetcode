class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        tmp, need = 0, (1 << 26) - 1
        for c in sentence:
            tmp |= 1 << (ord(c) - ord('a'))
            if tmp == need:
                return True
        return tmp == need