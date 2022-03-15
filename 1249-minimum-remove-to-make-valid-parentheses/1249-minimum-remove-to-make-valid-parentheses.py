class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ss = list(s)
        stk = []
        for i,c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                if stk:
                    stk.pop()
                else:
                    ss[i] = ''
        while stk:
            ss[stk.pop()] = ''
        return ''.join(ss)