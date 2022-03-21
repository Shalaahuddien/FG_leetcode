class Solution:
    def solveEquation(self, equation: str) -> str:
        lhs, rhs = equation.split("=")

        def fn(s):
            """Parse s into coefficients."""
            ii = x = y = 0
            for i in range(len(s) + 1):
                if i == len(s) or s[i] in "+-":
                    if ii < i:
                        y += int(s[ii:i])
                    ii = i
                elif s[i] == "x":
                    if ii == i or s[ii:i] in "+-":
                        x += int(s[ii:i] + "1")
                    else:
                        x += int(s[ii:i])
                    ii = i + 1
            return x, y

        (lx, ly), (rx, ry) = fn(lhs), fn(rhs)
        if lx == rx:
            if ly != ry:
                return "No solution"
            else:
                return "Infinite solutions"
        return f"x={(ry-ly)//(lx-rx)}"