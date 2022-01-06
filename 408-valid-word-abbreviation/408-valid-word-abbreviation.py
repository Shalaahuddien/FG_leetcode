class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        k = 0
        first = True
        while i < len(abbr):
            if abbr[i].isalpha():
                first = True
                j = j + k
                if j >= len(word):
                    return False
                k = 0
                if abbr[i] != word[j]:
                    return False
                j += 1
            else:
                if abbr[i] == "0" and first:
                    return False
                k = k * 10 + int(abbr[i])
                first = False
            i += 1
        return j + k == len(word)