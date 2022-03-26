class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        @cache
        def dc(N):
            if N == 1: return [1]
            left,right = dc((N+1)//2), dc(N//2)
            return [2*x-1 for x in left] + [2*x for x in right]
        return dc(n)