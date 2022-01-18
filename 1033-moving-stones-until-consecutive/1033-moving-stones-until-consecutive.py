class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        @cache
        def rec(abc):
            a, b, c = abc
            # base
            if b - a == c - b == 1:
                return [0, 0]
            elif (b - a == 1 and c - b > 1) or (b - a > 1 and c - b == 1):
                return [1, max(c - b - 1, b - a - 1)]
            # general (3 separated)
            mn1, _ = rec((b, b + 1, c))
            mn2, _ = rec((a, b - 1, b))
            _, mx1 = rec((a + 1, b, c))
            _, mx2 = rec((a, b, c - 1))
            return [min(mn1, mn2) + 1, max(mx1, mx2) + 1]

        abc = tuple(sorted([a, b, c]))
        return rec(abc)