class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk, res = [-1],0
        A = arr + [-1]
        for i,v in enumerate(A):
            while stk and A[stk[-1]] > v:
                idx = stk.pop()
                res += A[idx] * ((i-idx) * (idx-stk[-1]))
            stk.append(i)
        return res % (10**9+7)