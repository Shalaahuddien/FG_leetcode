class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for n in num:
            while k and stk and stk[-1] > n:
                stk.pop()
                k -= 1
            stk.append(n)
            
        finalStk = stk[:-k] if k else stk
        return ''.join(finalStk).lstrip('0') or '0'