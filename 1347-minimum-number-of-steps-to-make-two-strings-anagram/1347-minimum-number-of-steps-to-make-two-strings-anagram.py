class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = Counter(s)
        ans = len(t)
        for c in t:
            if c in freq and freq[c] != 0:
                freq[c] -= 1
                ans -= 1
        return ans