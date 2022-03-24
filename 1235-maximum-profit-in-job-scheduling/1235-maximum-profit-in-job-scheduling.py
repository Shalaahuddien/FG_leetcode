class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        start = [jobs[i][0] for i in range(n)]

        @cache
        def dp(i):
            if i == n:
                return 0
            ans = dp(i + 1)
            nxt = bisect_left(start, jobs[i][1])
            ans = max(ans, dp(nxt) + jobs[i][2])
            return ans

        return dp(0)