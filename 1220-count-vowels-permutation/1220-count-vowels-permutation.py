class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u, M = 1, 1, 1, 1, 1, 10**9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u)%M, (a + i)%M, (e + o)%M, i%M, (i + o)%M
        
        return (a + e + i + o + u)%M 