class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans, indices = -1, {}
        for i, c in enumerate(s):
            ans = max(ans, i - indices.setdefault(c, i) - 1)
        return ans