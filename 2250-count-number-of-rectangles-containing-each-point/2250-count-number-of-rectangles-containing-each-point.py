class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        h2l = defaultdict(list)
        for l, h in rectangles:
            h2l[h].append(l)
        cnt = [0] * len(points)
        for i, xy in enumerate(points):
            x, y = xy
            for h in range(y, 101):
                cnt[i] += len(h2l[h]) - bisect_left(h2l[h], x)
        return cnt