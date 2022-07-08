class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(i, j, k):
            # base case 1. the painted houses already formed > target neighborhoods
            if k > target:
                return math.inf

            # base case 2. we have painted m houses
            if i == m:
                # base case 2.1. these m houses form target neighborhoods exactly
                if k == target:
                    return 0
                # base case 2.2. these m houses form < target neighborhoods
                else:
                    return math.inf

            # case 1. the i-th house is already painted
            if houses[i]:
                return dp(i + 1, houses[i], k + (houses[i] != j))

            # case 2. we need to pick a color for the i-th house
            ans = math.inf
            for color, paint_cost in enumerate(cost[i], 1):
                ans = min(ans, paint_cost + dp(i + 1, color, k + (color != j)))

            return ans

        tmp = dp(0, 0, 0)
        return tmp if tmp < math.inf else -1