class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R,C = len(M), len(M[0])
        res = [[0]*C for _ in range(R)]
        dirs = [(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        for x in range(R):
            for y in range(C):
                tmp = [M[x+dx][y+dy] for dx,dy in dirs if 0 <= x+dx < R and 0 <= y+dy <C]
                res[x][y] = sum(tmp)//len(tmp)
        return res