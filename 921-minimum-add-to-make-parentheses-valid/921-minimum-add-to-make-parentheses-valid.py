class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count, ret = 0,0
        for c in s:
            if c == '(':
                count +=1
            else:
                count -=1
            if count == -1:
                ret += 1
                count = 0
        ret += count
        return ret