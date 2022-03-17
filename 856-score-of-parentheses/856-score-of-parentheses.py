class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal, ans = 0, 0
        for i,p in enumerate(s):
            if p =='(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    ans += 1 << bal
        return ans