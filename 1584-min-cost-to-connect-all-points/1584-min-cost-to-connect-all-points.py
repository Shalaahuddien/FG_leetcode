class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def man(i,j):
            pi,pj = points[i], points[j]
            return abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])
        
        pq = [(0, (0,0))]
        mst, n = 0, len(points)
        vis = set()
        while len(vis) < n:
            w, (u,v) = heappop(pq)
            if v in vis:
                continue
            mst += w
            vis.add(v)
            for i in range(n):
                if i not in vis and i != v:
                    heappush(pq, (man(v, i), (v,i)))
        return mst