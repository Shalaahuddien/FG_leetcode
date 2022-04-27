class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s, n, VOWS = s.lower(), len(s), set("aeiou")
        return sum(c in VOWS for c in s[: n // 2]) == sum(c in VOWS for c in s[n // 2 :])
