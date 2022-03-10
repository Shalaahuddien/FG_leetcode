class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]
        R, C = len(mat), len(mat[0])
        if r * c != R * C:
            return mat
        for i in range(R):
            for j in range(C):
                idx = i * C + j
                x, y = divmod(idx, c)
                res[x][y] = mat[i][j]
        return res
