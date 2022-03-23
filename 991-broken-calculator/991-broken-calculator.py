class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        def rec(t):
            if t <= startValue:
                return startValue - t
            if t % 2 == 1:
                return 1 + rec(t + 1)
            else:
                return 1 + rec(t // 2)

        return rec(target)