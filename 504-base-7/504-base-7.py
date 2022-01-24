class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        neg = num < 0
        x = abs(num)
        ans = []
        while x:
            x, m = divmod(x, 7)
            ans.append(str(m))
        ret = ''.join(ans[::-1])
        if neg:
            return '-' + ret
        return ret