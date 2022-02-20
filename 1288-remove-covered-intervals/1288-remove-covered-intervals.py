class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        x, y = -1, -1
        res = 0
        for l, r in intervals:
            if x <= l and r <= y:
                continue
            else:
                x, y = l, r
                res += 1

        return res