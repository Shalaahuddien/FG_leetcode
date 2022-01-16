class Solution:
    # from random import choice
    def __init__(self, w: List[int]):
        self.pre = [0] * (len(w)+1)
        for i in range(1, len(w)+1):
            self.pre[i] = self.pre[i-1] + w[i-1]

    def pickIndex(self) -> int:
        r = randint(1, self.pre[-1])
        i = bisect.bisect_left(self.pre, r)
        return i-1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()