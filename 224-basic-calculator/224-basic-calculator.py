class Solution:
    def calculate(self, s: str) -> int:
        def rec(q):
            sig,v,stk = '+', 0, []
            while q:
                c = q.popleft()
                if c.isdigit():
                    v = v*10 + int(c)
                if c == '(':
                    v = rec(q)
                if c in '+-)' or len(q) == 0:
                    if sig == '+':
                        stk.append(v)
                    elif sig == '-':
                        stk.append(-v)
                    sig = c
                    v = 0
                if c == ')':
                    break
            return sum(stk)
                
        return rec(deque(s))