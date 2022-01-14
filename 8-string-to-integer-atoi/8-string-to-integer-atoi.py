
NINF, INF = -int(2**31), int(2**31 - 1)

class Solution:
    def myAtoi(self, s: str) -> int:
        sig, v = 1, 0
        st = 0
        
        for c in s:
            if st == 0:
                if c == ' ':
                    pass
                elif c.isdigit():
                    st = 2
                    v = v*10 + int(c)
                elif c in '+-':
                    st = 1
                    if c == '-':
                        sig = -1
                else:
                    return 0
            elif st == 1:
                if c.isdigit():
                    st = 2
                    v = v*10 + int(c)
                else:
                    return 0
            elif st == 2:
                if c.isdigit():
                    st = 2
                    v = v*10 + int(c)
                else:
                    break
            else:
                return 0
            
        v = sig*v
        return max(NINF, min(INF, v))