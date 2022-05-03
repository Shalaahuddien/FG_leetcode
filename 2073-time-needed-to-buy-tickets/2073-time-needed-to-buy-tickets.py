class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        secs = 0
        for i, t in enumerate(tickets):
            if i <= k:
                secs += min(t, tickets[k])
            else:
                secs += min(t, tickets[k] - 1)
        return secs