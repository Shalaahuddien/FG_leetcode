class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # F = [1] + [0]*n
        F = [1, 0, 0]

        for i in range(1, n+1):
            # XXX: must init F[i%3] = 0 since 2 cases can be neither/single/both valid!
            F[i % 3] = 0
            if s[i-1:i] != '0':
                F[i % 3] = F[(i-1) % 3]
            if i-2 >= 0 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                F[i % 3] += F[(i-2) % 3]
        # print(F)
        return F[n % 3]