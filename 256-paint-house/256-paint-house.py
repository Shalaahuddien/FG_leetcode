class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def f(i,c):
            if i >= len(costs):
                return 0
            other = list(range(3))
            other.remove(c)
            return costs[i][c] + min([f(i+1,o) for o in other])
        if not costs:
            return 0
        return min([f(0,c) for c in range(3)])