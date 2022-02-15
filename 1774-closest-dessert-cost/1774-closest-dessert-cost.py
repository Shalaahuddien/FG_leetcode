class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        @cache
        def fn(i, cost):
            """
            Return sum of subsequence closest to target.
            """
            if cost >= target or i == len(tC):
                return cost
            return min(fn(i + 1, cost), fn(i + 1, cost + tC[i]), key=closest)

        tC = toppingCosts * 2
        closest = lambda x: (abs(x - target), x)
        ans = 1e6
        for b in baseCosts:
            ans = min(ans, fn(0, b), key=closest)
        return ans