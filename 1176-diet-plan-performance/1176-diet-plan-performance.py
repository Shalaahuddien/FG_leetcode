class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        def p(T):
            nonlocal points
            if T < lower:
                points -= 1
            elif T > upper:
                points += 1

        points = 0
        T = sum(calories[:k])
        p(T)
        for i in range(1, len(calories) - k + 1):
            T = T - calories[i - 1] + calories[i + k - 1]
            p(T)

        return points