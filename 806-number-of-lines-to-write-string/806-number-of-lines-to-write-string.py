class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        o = lambda c: ord(c) - ord("a")
        cur = 0
        res = [1, 0]
        for c in s:
            wid = widths[o(c)]
            cur += wid
            if cur > 100:
                cur = wid
                res[0] += 1
        res[1] = cur
        return res