class Solution:
    def minimumSum(self, num: int) -> int:
        def sum2slice(lis):
            return sum(int(''.join(map(str, li))) for li in lis)

        def bt(A, used, news, res):
            if len(used) == 4:
                mn = min(
                    sum2slice((news[:i], news[i:])) for i in range(1, 4))
                res.append(mn)
                return
            for i in range(4):
                if i > 0 and A[i - 1] == A[i] and i - 1 not in used:
                    continue
                if i not in used:
                    used.add(i)
                    bt(A, used, news + [A[i]], res)
                    used.remove(i)

        A = [int(c) for c in str(num)]
        A.sort()
        res = []
        bt(A, set(), [], res)
        return min(res)