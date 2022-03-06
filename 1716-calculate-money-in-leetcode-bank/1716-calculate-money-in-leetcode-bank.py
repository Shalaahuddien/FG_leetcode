class Solution:
    def totalMoney(self, n: int) -> int:
        tot = 0
        for d in range(1,n+1):
            i,j = divmod(d-1,7)
            tot += i + (j+1)
        return tot