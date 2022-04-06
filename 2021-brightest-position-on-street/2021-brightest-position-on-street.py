class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        points = []
        for p, r in lights:
            points.append((p - r, -1))
            points.append((p + r, 1))
        points.sort()
        mx = 0
        ans = -2e9
        sm = 0
        for i, flag in points:
            sm += 1 if flag == -1 else -1
            if sm > mx:
                mx = sm
                ans = i
        return ans
