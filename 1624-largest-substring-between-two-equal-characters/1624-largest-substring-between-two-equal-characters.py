class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        last_pos = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            last = last_pos[c]
            if i != last:
                ans = max(ans, last - i - 1)
        return ans