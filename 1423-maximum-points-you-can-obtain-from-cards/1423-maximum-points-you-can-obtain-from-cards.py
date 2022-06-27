class Solution:
    def maxScore(self, A, k):
        n, S = len(A), sum(A)
        ans = wind = sum(A[:n-k])
        for i in range(n-k, n):
            wind = wind - A[i-n+k] + A[i]
            ans = min(ans, wind)
        
        return S - ans