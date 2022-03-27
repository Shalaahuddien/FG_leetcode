class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(s, w):
            i, j, i2, j2 = 0, 0, 0, 0
            n, m = len(s), len(w)
            while i < n and j < m:
                if s[i] != w[j]:
                    return False
                while i2 < n and s[i2] == s[i]:
                    i2 += 1
                while j2 < m and w[j2] == w[j]:
                    j2 += 1
                if not (i2 - i == j2 - j or i2 - i >= max(3, j2 - j)):
                    return False
                i, j = i2, j2
            return i == n and j == m

        return sum(check(s, w) for w in words)