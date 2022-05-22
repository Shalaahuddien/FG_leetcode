class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")

        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                # BUG: return 2e9
                # XXX: INF+anything => INF.
                return INF
            return min(dp(i - c) + 1 for c in coins)

        return dp(amount) if dp(amount) != INF else -1