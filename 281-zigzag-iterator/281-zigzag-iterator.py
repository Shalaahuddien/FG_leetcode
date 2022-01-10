class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [deque(v1), deque(v2)]
        self.vec_idx = deque(range(len(self.v)))
        self.count = sum(len(x) for x in self.v)

    def next(self) -> int:
        idx = self.vec_idx.popleft()
        while not self.v[idx]:
            idx = self.vec_idx.popleft()
        v = self.v[idx].popleft()
        self.count -= 1
        self.vec_idx.append(idx)
        return v

    def hasNext(self) -> bool:
        return self.count > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())