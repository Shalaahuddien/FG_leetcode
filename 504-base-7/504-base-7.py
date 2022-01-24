class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = num < 0
        x = abs(num)
        ans = 0
        time = 1
        while x:
            x, m = divmod(x, 7)
            ans += time * m
            time *= 10
        ret = str(ans)
        if neg:
            return '-' + ret
        return ret