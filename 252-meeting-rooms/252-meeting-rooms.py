class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for prev, cur in zip(intervals, intervals[1:]):
            # BUG: equal is allowed
            if prev[1] > cur[0]:
                return False
        return True