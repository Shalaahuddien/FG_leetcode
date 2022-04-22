class MyHashMap:

    def __init__(self):
        self.hsize = int(1e3)
        self.rad = 33
        self.buckets = [[] for _ in range(self.hsize)]

    def _hash(self, n):
        d, q = self.rad, self.hsize
        h = 0
        while n:
            n, v = divmod(n, 10)
            h = (h * d + v) % q
        return h

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        self.remove(key)
        self.buckets[h].append((key, value))

    def get(self, key: int) -> int:
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                self.buckets[h].remove((k, v))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)