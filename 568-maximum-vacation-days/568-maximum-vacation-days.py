class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, K = len(days), len(days[0])
        F = [[i for i, can_fly in enumerate(city) if can_fly]
             for city in flights]

        @cache
        def backtrack(week, city):
            if week == K:
                return 0
            stay = days[city][week] + backtrack(week + 1, city)
            fly = max((days[other][week] + backtrack(week + 1, other)
                       for other in F[city]),
                      default=0)
            return max(stay, fly)

        return backtrack(0, 0)