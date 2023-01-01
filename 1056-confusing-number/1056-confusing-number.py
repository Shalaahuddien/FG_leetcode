class Solution:
    def confusingNumber(self, N: int) -> bool:
        x, y, cmap = N, 0, {0:0,1:1,6:9,8:8,9:6}
        while N:
            n, m = divmod(N, 10)
            if m not in cmap: return False
            N, y = n, y*10 + cmap[m]
        return x != y