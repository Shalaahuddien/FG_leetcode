class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = set("aeiouAEIOU")

        def vows(ss):
            cnt = 0
            for c in ss:
                if c in VOWELS:
                    cnt += 1
            return cnt

        return vows(s[: len(s) // 2]) == vows(s[len(s) // 2 :])
