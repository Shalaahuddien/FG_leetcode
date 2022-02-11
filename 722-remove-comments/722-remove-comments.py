class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        NORMAL, MLCOMMENT = 1,2
        st = NORMAL
        res = []
        
        buf = ''
        for s in source:
            i = 0
            while i < len(s):
                if st == NORMAL:
                    if s[i:i+2] == '//':
                        break
                    elif s[i:i+2] == '/*':
                        st = MLCOMMENT
                        i += 2
                    else:
                        buf += s[i]
                        i += 1
                else:
                    if s[i:i+2] == '*/':
                        st = NORMAL
                        i += 2
                    else:
                        i += 1
            
            if st == MLCOMMENT:
                pass
            else:
                if buf:
                    res.append(buf)
                    buf = ''
        return res