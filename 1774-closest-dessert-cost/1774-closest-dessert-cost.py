class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        opt = 1e6
        ans = 0
        for i in range(pow(3, len(toppingCosts))):
            topps, idx, cur = 0, i, 0
            while idx != 0:
                idx, q = divmod(idx, 3)
                topps += toppingCosts[cur] * (q)
                cur += 1
            for b in baseCosts:
                cost = topps + b
                if cost == target:
                    return cost
                if abs(cost - target) < abs(opt - target):
                    opt = cost
                elif abs(cost - target) == abs(opt - target):
                    opt = min(cost, opt)
        return opt