class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(k)->bool:
            t = 0
            for p in piles:
                t += math.ceil(p/k)
            return t <= h
        
        l,r = 1, max(piles)
        while l < r:
            k = (l+r)//2
            if f(k):
                r = k
            else:
                l = k+1
        return l
        