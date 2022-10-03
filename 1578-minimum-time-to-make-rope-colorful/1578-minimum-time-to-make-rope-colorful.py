class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = prev = 0  # index of previously retained letter
        s, cost = colors, neededTime
        for i in range(1, len(s)):
            if s[prev] != s[i]:
                prev = i
            else:
                ans += min(cost[prev], cost[i])
                if cost[prev] < cost[i]:
                    prev = i
        return ans