class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        def mxpq_push(v,x,y):
            heappush(mxpq, (-v,x,y))
        def mxpq_pop():
            negv, x,y = heappop(mxpq)
            return -negv, x,y
        
        mxpq = []
        seen = set([(0,0)])
        mxpq_push(grid[0][0],0,0)
        m,n = len(grid),len(grid[0])
        while mxpq:
            score, x,y = mxpq_pop()
            if (x,y) == (m-1,n-1):
                return score
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                xx,yy = x+dx,y+dy
                if 0<=xx<m and 0<= yy< n and (xx,yy) not in seen:
                    seen.add((xx,yy))
                    mxpq_push(min(score, grid[xx][yy]), xx,yy)
        return -1