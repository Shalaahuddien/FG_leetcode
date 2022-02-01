class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        num, den = abs(numerator), abs(denominator)

        n,r = divmod(num, den)
        res = [sign + str(n), '.']
        rs = {}
        while r > 0 and r not in rs:
            rs[r] = len(res)
            n,r = divmod(r*10, den)
            res.append(str(n))
        if r in rs:
            i = rs[r]
            res.insert(i, '(')
            res.append(')')
        return ''.join(res).rstrip('.')
        