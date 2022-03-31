class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        t = s.split("(")
        ans = t[0]
        for i in range(1, len(t)):
            a, b = t[i].split(")")
            ans += d.get(a, "?") + b
        return ans
