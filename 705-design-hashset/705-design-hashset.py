class MyHashSet:

    def __init__(self):
        self.hsize = 1999
        # self.hsize = int(1e6)  # XXX; all scientific notation num are float!

        self.rad = 33
        self.buckets = [[] for _ in range(self.hsize)]

    def _hash(self, n):
        d, q = self.rad, self.hsize
        h = 0
        while n:
            n, v = divmod(n, 10)
            h = (h * d + v) % q
        return h

    def add(self, key: int) -> None:
        h = self._hash(key)
        if not key in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.buckets[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)