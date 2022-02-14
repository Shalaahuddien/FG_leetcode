class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
            def count_bads(s):
                l, r = 0, 0
                for c in s:
                    if c == '(':
                        l += 1
                    elif c == ')':
                        r += 1
                        if l > 0:
                            l, r = l - 1, r - 1
                return l, r

            L, R = count_bads(s)
            ans = set()

            @cache
            def bt(s, l, r):
                if l == r == 0:
                    if (0, 0) == count_bads(s):
                        ans.add(s)
                        return
                for i in range(len(s)):
                    if s[i] in "()":
                        if l > 0:
                            bt(''.join(s[:i] + s[i + 1:]), l - 1, r)
                        if r > 0:
                            bt(''.join(s[:i] + s[i + 1:]), l, r - 1)

            bt(s, L, R)
            return ans

