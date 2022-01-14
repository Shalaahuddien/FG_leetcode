class Solution:
    def decodeString(self, s: str) -> str:
        # 3[a]
        # 3[a2[c]]
        
        def rec(q):
            res = ''
            k = 0
            while q:
                c = q.popleft()
                if c.isdigit():
                    k = k*10 + int(c)
                elif c == '[':
                    inner = rec(q)
                    res += k * inner
                    k = 0
                elif c.isalpha():
                    res += c
                else:
                    break
            return res
        return rec(deque(s))