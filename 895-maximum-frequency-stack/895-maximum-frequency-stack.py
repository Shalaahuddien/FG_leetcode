class FreqStack:

    def __init__(self):
        self.cnt_group = defaultdict(list)
        self.mx_cnt = 0
        self.v2cnt = defaultdict(int)

    def push(self, val: int) -> None:
        self.v2cnt[val] += 1
        f = self.v2cnt[val]
        self.cnt_group[f].append(val)
        self.mx_cnt = max(self.mx_cnt, f)

    def pop(self) -> int:
        f = self.mx_cnt
        v = self.cnt_group[f].pop()
        if not self.cnt_group[f]:
            del self.cnt_group[f]
            self.mx_cnt -= 1
        self.v2cnt[v] -= 1
        if self.v2cnt[v] == 0:
            del self.v2cnt[v]
        return v



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()