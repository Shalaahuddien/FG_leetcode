class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def bt(n):
            if n == 0:
                return False
            if n == isqrt(n)**2:
                return True
            for i in range(1, isqrt(n) + 1):
                if not bt(n - i**2):
                    return True
            return False

        return bt(n)