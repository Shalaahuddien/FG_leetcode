class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        res = max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - j[0] * i[1] - k[0] * j[1] - i[0] * k[1]) for i, j, k in combinations(p, 3))
        return res