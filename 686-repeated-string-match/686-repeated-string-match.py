class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = ceil(float(len(b)) / len(a))
        for t in (times, times + 1):
            if b in t * a:
                return t
        return -1