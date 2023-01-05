class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        itvs = sorted(points, key=lambda li: li[1])
        x_end = itvs[0][1]
        count = 1
        for start, end in itvs:
            if start > x_end:
                count += 1
                x_end = end
        return count