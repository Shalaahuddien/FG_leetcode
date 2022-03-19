"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        from sortedcontainers import SortedDict

        sd = SortedDict()
        for sch in schedule:
            for itv in sch:
                s, f = itv.start, itv.end
                sd[s] = sd.setdefault(s, 0) + 1
                sd[f] = sd.setdefault(f, 0) - 1
        res = []
        start, score = -1, 0
        for k, v in sd.items():
            score += v
            if score == 0 and start == -1:
                start = k
            elif start != -1 and score != 0:
                res.append(Interval(start, k))
                start = -1
        return res