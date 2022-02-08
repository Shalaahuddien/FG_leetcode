class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sumdig(v):
            return sum(map(int, str(v)))

        k0 = int(''.join([str(ord(c) - ord('a') + 1) for c in s]))
        for _ in range(k):
            k0 = sumdig(k0)
        return k0