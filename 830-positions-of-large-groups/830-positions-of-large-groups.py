class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        i = 0
        for j in range(len(s)):
            if j == len(s)-1 or s[j] != s[j+1]:
                if j -i+1>= 3:
                    res.append([i,j])
                i = j+1
        return res