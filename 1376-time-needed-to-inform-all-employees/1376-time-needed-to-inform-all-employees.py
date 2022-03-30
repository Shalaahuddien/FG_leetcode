class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def dfs(e):
            m = manager[e]
            if m == -1:
                return 0
            return informTime[m] + dfs(m)

        return max(map(dfs, range(n)))