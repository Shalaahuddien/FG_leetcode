class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pq = []
        for s,f in sorted(intervals, key=lambda x: x[0]):
            if pq and pq[0] <= s:
                heappushpop(pq, f)
            else:
                heappush(pq, f)
        return len(pq)
        