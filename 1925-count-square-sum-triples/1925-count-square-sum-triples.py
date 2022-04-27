class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(3, n + 1):
            for b in range(a + 1, n + 1):
                c2 = a * a + b * b
                c = sqrt(c2)
                if int(c) == c and c2 <= n * n:
                    ans += 2
        return ans