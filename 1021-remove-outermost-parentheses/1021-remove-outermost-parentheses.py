class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0
        for c in s:
            if c == "(":
                if count != 0:
                    res.append(c)
                count += 1
            else:
                if count != 1:
                    res.append(c)
                count -= 1
        return "".join(res)