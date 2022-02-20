class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        preend = 0
        remain = 0
        for _,r in intervals:
            if r > preend:
                preend = r
                remain += 1
        return remain