class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def match(i1, i2):
            if i1 == n1 and i2 == n2: return True
            return i1 < n1 and s1[i1] == s3[i1 + i2] and match(i1 + 1, i2) or i2 < n2 and s2[i2] == s3[i1 + i2] and match(i1, i2 + 1)

        n1, n2 = len(s1), len(s2)
        return n1 + n2 == len(s3) and match(0, 0)