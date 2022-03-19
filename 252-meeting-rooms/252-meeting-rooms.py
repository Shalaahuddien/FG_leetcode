class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        from sortedcontainers import SortedDict

        sd = SortedDict()
        for s, f in intervals:
            sd[s] = sd.setdefault(s, 0) + 1
            sd[f] = sd.setdefault(f, 0) - 1
        room = 0
        for _, v in sd.items():
            room += v
            if room > 1:
                return False
        return True