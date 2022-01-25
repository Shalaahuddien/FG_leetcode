class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        P = [0] * (len(s)+1)
        for i,c in enumerate(s):
            P[i+1] = P[i] + int(c)
            
        return min(
            P[j] + len(s)-j-(P[-1]-P[j]) for j in range(len(P))
        )