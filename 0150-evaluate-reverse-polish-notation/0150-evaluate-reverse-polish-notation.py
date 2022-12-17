class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ O(N)TS """
        stack, ops = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for t in tokens:
            if str.isnumeric(t) or (len(t) > 1 and t[0] == '-'):
                stack += int(t),
            else:
                fn, y, x = ops[t], stack.pop(), stack.pop()
                stack += int(fn(x, y)),

        return stack.pop()