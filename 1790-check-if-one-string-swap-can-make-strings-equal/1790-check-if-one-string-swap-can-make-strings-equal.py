class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not dif or len(dif) == 2 and dif[0][::-1] == dif[1]
