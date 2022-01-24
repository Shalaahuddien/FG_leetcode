class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        if len(s) < 4:
            return s

        s = s[::-1]
        ret = [None] * len(s)
        for i in range(len(s)):
            ret[i] = s[i]
            if (i + 1) % 3 == 0:
                ret[i] += '.'
        ans = ''.join(ret)[::-1]
        if ans[0] == '.':
            return ans[1:]
        return ans