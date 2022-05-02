class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ci = [i for i, c in enumerate(s) if c.isalpha()]
        l, r = 0, len(ci) - 1
        lc = list(s)
        while l < r:
            i, j = ci[l], ci[r]
            lc[i], lc[j] = lc[j], lc[i]
            l, r = l + 1, r - 1
        return "".join(lc)