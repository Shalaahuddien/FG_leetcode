class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
        return sum(map(lambda x: bin(x).count("1") in PRIMES, range(left, right + 1)))