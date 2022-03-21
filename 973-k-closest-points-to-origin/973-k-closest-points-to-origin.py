class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(co):
            return co[0] ** 2 + co[1] ** 2

        points.sort(key=dist)
        return points[:k]