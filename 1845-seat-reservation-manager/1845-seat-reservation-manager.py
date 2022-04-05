class SeatManager:

    def __init__(self, n: int):
        self.mnpq = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.mnpq)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.mnpq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)