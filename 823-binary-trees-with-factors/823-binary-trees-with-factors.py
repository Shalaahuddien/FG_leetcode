class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d = {n: i for i, n in enumerate(arr)}
        MOD = 10**9 + 7

        @cache
        def dp(i):
            root = arr[i]
            cnt = 1
            for x in arr[:i]:
                if root % x == 0 and root // x in d:
                    # if x * x == root:
                    #     cnt += dp(d[x])
                    # else:
                    cnt += dp(d[x]) * dp(d[root // x])
            return cnt % MOD

        return sum(dp(i) for i in range(len(arr))) % MOD