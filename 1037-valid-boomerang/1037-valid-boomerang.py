class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        A, B, C = points[0], points[1], points[2]
        return (B[1] - A[1]) * (B[0] - C[0]) != (B[1] - C[1]) * (B[0] - A[0])
