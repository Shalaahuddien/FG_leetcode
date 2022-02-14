class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def dfs(ti, p, cost, res):
            nonlocal ans, diff
            if abs(cost - target) < diff:
                ans = cost
                diff = abs(cost - target)
            elif abs(cost - target) == diff:
                ans = min(ans, cost)
            # add all combi to res
            res.append(cost)
            if ti == len(toppingCosts):
                return
            if cost > target:
                return
            for pick in range(3):
                dfs(ti + 1, pick, cost + toppingCosts[ti] * pick, res)

        res = []
        ans = diff = 1e6
        for b in baseCosts:
            dfs(0, 0, b, res)
        return ans