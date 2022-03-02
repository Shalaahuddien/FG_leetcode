class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
        return sum(1 for n in range(left, right + 1) if bin(n).count("1") in PRIMES)