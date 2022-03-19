from sortedcontainers import SortedDict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sd = SortedDict()
        for s, f in intervals:
            sd[s] = sd.setdefault(s, 0) + 1
            sd[f] = sd.setdefault(f, 0) - 1
        room, k = 0, 0
        for _, v in sd.items():
            room += v
            k = max(k, room)
        return k