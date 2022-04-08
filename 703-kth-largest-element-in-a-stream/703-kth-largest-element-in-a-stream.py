class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mnpq = []
        self.k = k
        for n in nums:
            heappush(self.mnpq, n)
            if len(self.mnpq) > k:
                heappop(self.mnpq)

    def add(self, val: int) -> int:
        if len(self.mnpq) < self.k:
            heappush(self.mnpq, val)
        else:
            heappushpop(self.mnpq, val)
        return self.mnpq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)