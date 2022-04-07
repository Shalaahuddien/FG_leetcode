class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mxheap = []
        for s in stones:
            heappush(mxheap, -s)
        while len(mxheap) >= 2:
            y = -heappop(mxheap)
            x = -heappop(mxheap)
            if x == y:
                pass
            elif x != y:
                heappush(mxheap, -(y - x))
        # return -mxheap[0]
        return -heappop(mxheap) if mxheap else 0