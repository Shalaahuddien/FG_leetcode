class Solution:

    def __init__(self, w: List[int]):
        # T: O(N), M: O(N)
        self.P = [0] * (len(w) + 1)
        for i in range(len(w)):
            self.P[i + 1] = self.P[i] + w[i]

    def pickIndex(self) -> int:
        # T: O(logN)
        r = randint(1, self.P[-1])
        i = bisect.bisect_left(self.P, r)
        return i - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()