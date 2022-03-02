class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        difa, difb = [], []
        for x, y in zip(s1, s2):
            if x != y:
                difa.append(x)
                difb.append(y)
            if len(difa) > 2:
                return False
        return len(difa) == 0 or len(difa) == 2 and difa == difb[::-1]
