class ZigzagIterator:
    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.data)
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())