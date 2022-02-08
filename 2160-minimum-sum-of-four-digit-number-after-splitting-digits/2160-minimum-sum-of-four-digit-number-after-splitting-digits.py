class Solution:
    def minimumSum(self, num: int) -> int:
        def sum2slice(lis):
            return sum(int(''.join(map(str, li))) for li in lis)

        perms = permutations([int(c) for c in str(num)])

        mn = 9999
        for p in perms:
            mn = min(mn,
                     min(sum2slice((p[:i], p[i:])) for i in range(1, 4)))
        return mn