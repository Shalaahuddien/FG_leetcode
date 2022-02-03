class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = OrderedDict()
        self.is_uniq = {}
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if self.q:
            # XXX: next/iter, so you don't need global pointer!
            return next(iter(self.q))
        return -1

    def add(self, value: int) -> None:
        # case 1: we need to add v into q, and mark it unique
        if value not in self.is_uniq:
            self.is_uniq[value] = True
            self.q[value] = None
        # case 2: we need to mark it duplicate, then remove it from queue
        elif self.is_uniq[value]:
            self.is_uniq[value] = False
            self.q.pop(value)
        # case 3: do nothing!    


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)