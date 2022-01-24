class Solution:
    def convertToBase7(self, num: int) -> str:
        x, ans, time = abs(num), 0, 1
        while x:
            x, m = divmod(x, 7)
            ans += time * m
            time *= 10
        ret = str(ans)
        return '-' * (num < 0) + ret