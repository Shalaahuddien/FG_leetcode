class Solution:
    def calculate(self, s: str) -> int:
        def rec(q):
            num, sign = 0, "+"
            stk = []
            while q:
                c = q.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == "(":
                    num = rec(q)
                if c in "+-*/)" or not q:
                    #! careful we catch ')' to eval (...), ow  (4-5/2) will only be sum([4,-5]) => -1, /2 is ignored
                    if sign == "+":
                        stk.append(num)
                    elif sign == "-":
                        stk.append(-num)
                    elif sign == "*":
                        stk[-1] = stk[-1] * num
                    elif sign == "/":
                        stk[-1] = int(stk[-1] / float(num))
                    sign = c
                    num = 0
                if c == ")":
                    break

            return sum(stk)

        return rec(deque(s))