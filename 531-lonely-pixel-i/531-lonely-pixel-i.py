class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        col = [0] * n
        row = set()
        for i in range(m):
            cnt = 0
            for j in range(n):
                if picture[i][j] == 'B':
                    c = j
                    cnt += 1
                    col[j] += 1
            if cnt == 1: row.add(c)
        ans = 0        
        for i, c in enumerate(col):
            if c == 1 and i in row:
                ans += 1
        return ans  