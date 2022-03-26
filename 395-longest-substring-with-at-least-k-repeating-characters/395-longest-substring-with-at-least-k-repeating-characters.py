class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dc(s):
            if len(s) < k:
                return ""
            freq = Counter(s)
            for i, c in enumerate(s):
                if freq[c] < k:
                    sl = dc(s[:i])
                    sr = dc(s[i + 1 :])
                    return max(sl, sr, key=len)
            return s

        return len(dc(s))