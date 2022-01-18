class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for p in path.split('/'):
            if p in ('', '.'):
                continue
            elif p == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(p)
        return '/' + '/'.join(stk)