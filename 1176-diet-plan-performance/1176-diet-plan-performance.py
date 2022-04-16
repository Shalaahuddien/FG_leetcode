class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        point, win = 0, 0
        for i, cal in enumerate(calories):
            win += cal
            if i >= k - 1:
                if i > k - 1:
                    win -= calories[i - k]
                if win < lower:
                    point -= 1
                elif win > upper:
                    point += 1
        return point