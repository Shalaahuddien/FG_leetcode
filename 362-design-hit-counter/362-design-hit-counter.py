class HitCounter:

    def __init__(self):
        self.wind = deque()

    def _pop_old(self, ts):
        while self.wind:
            if ts - 300 + 1 > self.wind[0]:
                self.wind.popleft()
            else:
                break

    def hit(self, timestamp: int) -> None:
        self.wind.append(timestamp)
        self._pop_old(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._pop_old(timestamp)
        lo, hi = timestamp - 300 + 1, timestamp
        """
        range_count_query (common pattern of bisect usage)
        count(lo...hi) = count(<=hi) - count(<lo)
        reminds me of slide-window exact(k) = atMost(k) - atMost(k-1)
        """
        return bisect_right(self.wind, hi) - bisect_left(self.wind, lo)



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)