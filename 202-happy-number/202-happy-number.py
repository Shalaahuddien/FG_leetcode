class Solution:
    def isHappy(self, n: int) -> bool:
        def nex(n):
            r = 0
            while n:
                n,dig = divmod(n,10)
                r += dig**2
            return r
        
        s=f=n
        while f!= 1:
            s = nex(s)
            f = nex(nex(f))
            if s == f:
                break
        return f == 1