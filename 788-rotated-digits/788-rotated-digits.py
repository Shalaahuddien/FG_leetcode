class Solution:
    def rotatedDigits(self, n: int) -> int:
        d = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

        def rev(v):
            vv = str(v)

            ans = 0
            for c in vv:
                if int(c) not in d:
                    return -1
                ans = ans * 10 + d[int(c)]
            return ans

        ans = []
        for i in range(1, n + 1):
            ri = rev(i)
            # print(i, ri)
            if ri not in (-1, i):
                ans.append(i)
        return len(ans)