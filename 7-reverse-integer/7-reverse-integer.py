class Solution:
    def reverse(self, x: int) -> int:
        sig = 1 if x >= 0 else -1
        n = abs(x)
        rev = 0
        while n:
            n, m = divmod(n, 10)
            rev = rev * 10 + m

            if sig == -1:
                if rev * sig < -2**31:
                    return 0
            else:
                if rev > 2**31 - 1:
                    return 0
        return rev * sig
