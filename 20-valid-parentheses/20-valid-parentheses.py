class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stk = []
        pas = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c not in pas:
                stk.append(c)
            else:
                if not stk or pas[c] != stk.pop():
                    return False
        return not stk