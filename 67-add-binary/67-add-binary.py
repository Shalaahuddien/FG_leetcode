class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        ans = []
        aa = a[::-1]
        bb = b[::-1]
        if len(aa) > len(bb):
            aa, bb = bb, aa
        for i in range(len(aa)):
            x, y = int(aa[i]), int(bb[i])
            c, v = divmod(x + y + c, 2)
            ans.append(v)
        for j in range(i + 1, len(bb)):
            x, y = int(bb[j]), 0
            c, v = divmod(x + y + c, 2)
            ans.append(v)
        if c:
            ans.append(c)
        return ''.join(str(v) for v in ans)[::-1]