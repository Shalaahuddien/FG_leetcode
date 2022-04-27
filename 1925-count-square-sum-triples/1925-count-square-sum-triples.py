class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(3, n + 1):
            for b in range(a + 1, n + 1):
                c2 = a**2 + b**2
                c = isqrt(c2)
                if c**2 == c2 and c2 <= n**2:
                    ans += 2
        return ans