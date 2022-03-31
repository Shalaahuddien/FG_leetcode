class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        l, r = 0, 0
        res = []
        d = {}
        for q, a in knowledge:
            d[q] = a
        print(d)
        while l < len(s):
            if s[l] == "(":
                l += 1
                r = l
                while r < len(s) and s[r] != ")":
                    r += 1
                # r oor or s[r] != ')'
                if r < len(s) and s[r] == ")":
                    res.append(d.get(s[l:r], "?"))
                    r += 1
                l = r
            else:
                res.append(s[l])
                l += 1
        return "".join(res)