class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                c = chr(int(s[i - 2 : i]) - 10 + ord("j"))
                res.append(c)
                i -= 3
            else:
                c = chr(int(s[i]) - 1 + ord("a"))
                res.append(c)
                i -= 1
        return "".join(res[::-1])