class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.d = {}
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey == self.ptr:
            sb = [value]
            i = idKey + 1
            while i <= self.n:
                if i in self.d:
                    sb.append(self.d[i])
                    i += 1
                else:
                    break
            self.ptr = i
            return sb
        else:
            self.d[idKey] = value
            return []




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)