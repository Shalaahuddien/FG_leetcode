class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])
        
        arrows = 1
        x_end = points[0][1]
        for s,e in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if s > x_end:
                arrows += 1
                x_end = e
        
        return arrows