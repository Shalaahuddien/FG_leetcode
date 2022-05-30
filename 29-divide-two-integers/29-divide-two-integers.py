class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend, divisor) == (-2**31, -1): # only case of overflow
            return 2**31 - 1
        neg = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        while dividend >= divisor:
            q, acc = 1, divisor
            while dividend >= (acc<<1):
                q <<= 1
                acc <<= 1
            res += q
            dividend -= acc
                
        return [1,-1][neg]*res