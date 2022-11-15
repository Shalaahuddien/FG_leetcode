class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        max_less_than_k, i, j = -1, 0, len(A)-1
        while i < j:
            S = A[i] + A[j]
            if S < K:
                max_less_than_k = max(max_less_than_k, S)
                i += 1
            else:
                j -= 1
        return max_less_than_k