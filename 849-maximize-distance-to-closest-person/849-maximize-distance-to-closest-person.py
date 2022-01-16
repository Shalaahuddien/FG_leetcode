class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, res = -1, 0
        for i,s in enumerate(seats):
            if s == 1:
                if prev < 0:
                    res = i
                else:
                    res = max(res, (i-prev)//2)
                prev = i
        res = max(res, i - prev)
        return res