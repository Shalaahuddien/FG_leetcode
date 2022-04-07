class HitCounter:
    def __init__(self):
        self.q = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.q:
            diff = timestamp - self.q[0][0]
            if diff >= 300:
                x = self.q.popleft()
                self.total -= x[1]
            else:
                break
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)