class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        x = isqrt(n)
        # check if n is square number
        if x * x != n:
            return False
        # check if n is square of PRIME, so check if x is PRIME
        for i in range(2, isqrt(x) + 1):
            if x % i == 0:
                return False
        return True