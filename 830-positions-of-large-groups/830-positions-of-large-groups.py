class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        pre, idx = "", 0
        res = []
        for i, c in enumerate(s + "*"):
            if pre != c:
                if pre and i - idx >= 3:
                    res.append([idx, i - 1])
                pre, idx = c, i
        return res