class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def letter_get(ch, dir):
            n = len(s)
            res, cur = [0] * n, -n
            for i in range(n)[::dir]:
                if s[i] == ch:
                    cur = i
                res[i] = abs(i - cur)
            return res

        return [min(x, y) for x, y in zip(letter_get(c, 1), letter_get(c, -1))]
