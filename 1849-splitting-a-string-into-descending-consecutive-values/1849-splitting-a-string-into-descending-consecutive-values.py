class Solution:
    def splitString(self, s: str) -> bool:
        def bt(s, i,l,prev,splits):
            if i == len(s) and splits >= 2:
                return True
            
            while i +l <= len(s):
                cur = int(s[i:i+l])
                l += 1
                if prev != -1 and cur != prev-1:
                    continue
                if bt(s, i+l-1, 1, cur, splits+1):
                    return True
                
            return False
        
        return bt(s, 0, 1, -1, 0)
            