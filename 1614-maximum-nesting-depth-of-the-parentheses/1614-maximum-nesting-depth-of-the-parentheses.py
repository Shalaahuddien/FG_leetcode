class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        stk = []
        for c in s:
            if c == '(':
                stk.append(c)
                mx = max(mx, len(stk))
            elif c == ')':
                stk.pop()
        return mx