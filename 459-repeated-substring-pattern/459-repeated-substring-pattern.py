class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N=  len(s)
        for l in range(1, N//2+1):
            if N%l==0 and s[:l]*(N//l) == s:
                return True
        return False