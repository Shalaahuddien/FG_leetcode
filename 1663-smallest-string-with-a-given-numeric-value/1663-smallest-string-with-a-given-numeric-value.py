class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = [None]*n
        for i in range(n-1,-1,-1):
            add = min(k-i, 26)
            res[i] = chr(add-1+ord('a'))
            k -= add
        return ''.join(res)