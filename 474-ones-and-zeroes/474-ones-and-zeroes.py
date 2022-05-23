class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [(s.count("0"), s.count("1")) for s in strs]

        @cache
        def dp(mm, nn, kk):
            """
            The order of two conditions matter. ow, it fails with test case:
            ["10","0001","111001","1","0"]
            4
            3
            """
            if mm < 0 or nn < 0:
                return float("-inf")
            if kk == len(strs):
                return 0
            z, o = xy[kk]
            return max(1 + dp(mm - z, nn - o, kk + 1), dp(mm, nn, kk + 1))

        return dp(m, n, 0)