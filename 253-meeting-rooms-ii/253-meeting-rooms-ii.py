class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        pq = []
        for itv in sorted(intervals, key=lambda tu: tu[0]):
            if pq and pq[0] <= itv[0]:
                heappushpop(pq, itv[1])
            else:
                heapq.heappush(pq, itv[1])
        return len(pq)