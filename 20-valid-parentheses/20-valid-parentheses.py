class Solution:
    def isValid(self, s: str) -> bool:
        open = '([{'
        close = ')]}'
        oc = {c:o for o,c in zip(open,close)}
        stk = []
        for c in s:
            if c in open:
                stk.append(c)
            else:
                if not stk:
                    return False
                op = stk.pop()
                if oc[c] != op:
                    return False
                
        return not stk
                