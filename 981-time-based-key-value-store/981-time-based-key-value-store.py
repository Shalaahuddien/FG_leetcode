class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ltv = self.kv[key]
        i = bisect_right(ltv, timestamp, key=lambda x: x[0])
        i -= 1
        if i < 0:
            return ''
        ts, val = ltv[i]
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)