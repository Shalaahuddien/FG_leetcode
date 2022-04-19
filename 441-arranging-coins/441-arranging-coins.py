class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 1
        comp = 0
        while n:
            if r <= n:
                comp += 1
            n -= min(r, n)
            r += 1
        return comp
