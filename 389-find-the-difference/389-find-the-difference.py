class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs, ct = Counter(s), Counter(t)
        for k, v in cs.items():
            ct[k] -= v
        for k, v in ct.items():
            if v == 1:
                return k