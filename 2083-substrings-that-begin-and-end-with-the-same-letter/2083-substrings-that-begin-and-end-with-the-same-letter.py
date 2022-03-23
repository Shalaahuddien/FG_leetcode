class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        C = Counter(s)
        ans = len(s)
        for c, f in C.items():
            ans += f * (f - 1) // 2
        return ans