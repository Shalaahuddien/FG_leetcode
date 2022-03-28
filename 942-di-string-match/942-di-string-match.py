class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lo, hi = 0, n
        res = []
        for i, c in enumerate(s):
            if c == "I":
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        return res + [lo]
