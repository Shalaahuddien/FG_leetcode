class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for c in s:
            x ^= ord(c)
        for c in t:
            x ^= ord(c)
        return chr(x)