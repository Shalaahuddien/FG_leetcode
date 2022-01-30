class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        h = 0
        i = 0
        p = 1
        while i < k:
            h += (ord(s[i]) - ord('a') + 1) * p
            i += 1
            p *= power

        p //= power

        if h % modulo == hashValue:
            return s[:k]

        while i < len(s):
            h -= (ord(s[i - k]) - ord('a') + 1)
            h //= power
            h += (ord(s[i]) - ord('a') + 1) * p
            if h % modulo == hashValue:
                return s[i - k + 1:i + 1]
            i += 1