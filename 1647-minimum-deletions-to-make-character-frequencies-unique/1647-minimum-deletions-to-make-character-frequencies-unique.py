class Solution:
    def minDeletions(self, s: str) -> int:
        prev, keep = 2e9, 0
        for freq in sorted(Counter(s).values(), reverse=True):
            freq = min(prev - 1, freq)
            if freq == 0:
                break
            keep += freq
            prev = freq
        return len(s) - keep