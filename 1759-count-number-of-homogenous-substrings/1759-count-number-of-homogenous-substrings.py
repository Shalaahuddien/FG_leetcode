class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        MOD = 10**9+7
        for c,grp in groupby(s):
            n = len(list(grp))
            res += (n+1)*n//2
            res %= MOD
        return res