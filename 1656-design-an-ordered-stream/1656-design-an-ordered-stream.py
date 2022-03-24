class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 0  # base-0
        self.d = [None] * n

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1  # base-0
        self.d[id] = value
        if id > self.ptr:
            return []

        while self.ptr < len(self.d) and self.d[self.ptr]:
            self.ptr += 1
        return self.d[id : self.ptr]



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)