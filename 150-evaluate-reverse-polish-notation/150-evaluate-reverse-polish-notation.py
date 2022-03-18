class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stk = []
        for tok in tokens:
            if tok in ops:
                sec = stk.pop()
                fir = stk.pop()
                op = ops[tok]
                stk.append(op(fir, sec))
            else:
                stk.append(int(tok))
        return stk[-1]