class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(s: str):
            cnt = Counter()
            num = coeff = ""
            is_x = False
            for i in range(len(s) - 1, -1, -1):
                if s[i] in "+-":
                    sign = 1
                    if s[i] == "-":
                        sign = -1
                    if is_x:
                        cnt["x"] += sign * (int(coeff) if coeff else 1)
                    else:
                        cnt["const"] += sign * int(num)
                    coeff = num = ""
                    is_x = False
                elif s[i] == "x":
                    is_x = True
                else:
                    if is_x:
                        coeff = s[i] + coeff
                    else:
                        num = s[i] + num
            return cnt

        lhs, rhs = equation.split("=")
        if lhs[0] not in "+-":
            lhs = "+" + lhs
        if rhs[0] not in "+-":
            rhs = "+" + rhs
        cl, cr = parse(lhs), parse(rhs)
        # print(cl, cr)

        cl["x"] -= cr["x"]
        cr["const"] -= cl["const"]
        if cl["x"] == 0:
            if cr["const"] != 0:
                return "No solution"
            return "Infinite solutions"
        ans = cr["const"] // cl["x"]
        return f"x={ans}"