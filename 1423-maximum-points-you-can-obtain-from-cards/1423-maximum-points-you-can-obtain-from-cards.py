class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot = sum(cardPoints)
        M = len(cardPoints)
        N = M - k
        mn = 0
        for i in range(N):
            mn += cardPoints[i]
        sm = mn
        for i in range(1, M - N + 1):
            sm = sm - cardPoints[i - 1] + cardPoints[i + N - 1]
            mn = min(sm, mn)
        return tot - mn