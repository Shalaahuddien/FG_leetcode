class Solution:
    def multiply(self, A: str, B: str) -> str:
        if '0' in {A,B}:
            return '0'
        res = [0] * (len(A)+len(B))
        for i,x in enumerate(A[::-1]):
            for j,y in enumerate(B[::-1]):
                xy = int(x)*int(y) + res[i+j]
                ten,one = divmod(xy,10)
                res[i+j+1] += ten
                res[i+j] = one
        
        if res[-1] == 0:
            res.pop()
        return ''.join(map(str, res[::-1]))
         
                