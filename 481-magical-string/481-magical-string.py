class Solution:
    def magicalString(self, n: int) -> int:
        s = [1,2,2]
        idx = 2
        while len(s) < n:
            x = 3-s[-1]
            times = s[idx]
            s += [x] * times
            idx += 1
        return s[:n].count(1)
        