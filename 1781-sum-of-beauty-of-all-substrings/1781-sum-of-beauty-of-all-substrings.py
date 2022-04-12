class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0

        def beauty(f):
            return max(f.values()) - min(f.values())

        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                ans += beauty(freq)
        return ans