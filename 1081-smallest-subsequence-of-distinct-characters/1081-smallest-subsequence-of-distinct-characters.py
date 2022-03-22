class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)}
        stk = []
        instk = set()
        for i,c in enumerate(s):
            if c in instk:
                continue
            while stk and stk[-1] > c:
                if last[stk[-1]] > i:
                    instk.remove(stk.pop())
                else:
                    break
            stk.append(c)
            instk.add(c)
        return ''.join(stk)