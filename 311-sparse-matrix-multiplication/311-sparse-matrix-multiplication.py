class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        I, J = len(mat1), len(mat1[0])
        K = len(mat2[0])
        ans = [[0] * K for _ in range(I)]

        for i in range(I):
            for j in range(J):
                if mat1[i][j]:
                    for k in range(K):
                        ans[i][k] += mat1[i][j] * mat2[j][k]
        return ans