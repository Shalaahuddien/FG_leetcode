class Solution:
    def confusingNumber(self, n: int) -> bool:
        mp = {0:0, 1:1, 6:9,8:8,9:6}
        y = n
        x = 0
        while n:
            n,m = divmod(n,10)
            if m not in mp:
                return False
            x = x*10 + mp[m]
        return x != y