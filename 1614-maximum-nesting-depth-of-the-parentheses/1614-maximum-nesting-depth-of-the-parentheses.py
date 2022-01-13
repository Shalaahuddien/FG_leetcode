class Solution:
    def maxDepth(self, s: str) -> int:
        mx = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                mx = max(mx, cur)
            elif c == ')':
                cur -= 1
        return mx