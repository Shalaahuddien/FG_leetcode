class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = win = 0
        L = len(cardPoints)
        for i in range(L - k, L + k):
            win += cardPoints[i % L]
            if i >= L:
                win -= cardPoints[i - k]
            ans = max(win, ans)
        return ans
