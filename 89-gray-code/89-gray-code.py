class Solution:
    def grayCode(self, n: int) -> List[int]:
        def rec(b):
            if b == 0:
                return [0]
            t = rec(b-1)
            return t + [(1<<(b-1)) + n for n in t][::-1]
        return rec(n)