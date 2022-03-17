class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        @cache
        def F(i,j):
            ans, bal = 0,0
            for k in range(i,j):
                bal += 1 if s[k] == '(' else -1
                if bal == 0:
                    if k-i == 1:
                        ans += 1
                    else:
                        ans += 2*F(i+1, k)
                    i = k+1
            return ans
        return F(0, len(s))