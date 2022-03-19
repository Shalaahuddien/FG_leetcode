class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.mx_freq = 0
        self.group = defaultdict(list)

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        self.mx_freq = max(f, self.mx_freq)
        self.group[f].append(val)

    def pop(self) -> int:
        x  = self.group[self.mx_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.mx_freq]:
            self.mx_freq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()