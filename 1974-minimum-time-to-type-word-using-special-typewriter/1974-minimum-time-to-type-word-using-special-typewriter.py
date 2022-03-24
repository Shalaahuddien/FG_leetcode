class Solution:
    def minTimeToType(self, word: str) -> int:
        def o(c):
            return ord(c) - ord("a")

        a = "a"
        cost = 0
        for c in word:
            d1 = abs(o(c) - o(a))
            d2 = 0
            if o(c) > o(a):
                d2 = abs(o(c) - (o("z") + 1 + o(a)))
            else:
                d2 = abs(o(a) - (o("z") + 1 + o(c)))
            cost += min(d1, d2) + 1
            a = c
        return cost