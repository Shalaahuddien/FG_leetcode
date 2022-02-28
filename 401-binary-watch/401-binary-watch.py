class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        @cache
        def bt(left, hh, mm):
            if hh >= 12 or mm > 59:
                return
            if left == 0:
                res.add(f'{hh}:{mm:02d}')
                return
            for h, m in product(range(4), range(6)):
                if (1 << h) & hh == 0:
                    bt(left - 1, hh | (1 << h), mm)
                if (1 << m) & mm == 0:
                    bt(left - 1, hh, (1 << m) | mm)

        res = set()
        bt(turnedOn, 0, 0)
        return sorted(list(res))