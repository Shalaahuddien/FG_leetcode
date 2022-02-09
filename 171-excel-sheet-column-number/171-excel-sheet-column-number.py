class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pos = 0
        res = 0
        for c in reversed(columnTitle):
            res += (ord(c) - ord('A') + 1) * (26**pos)
            pos += 1
        return res