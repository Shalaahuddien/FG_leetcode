class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90():
            n = len(mat)
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1], mat[n - j - 1][i] = mat[n - j - 1][i], mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1]
            # [(i, j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]

        n = len(mat)
        for _ in range(4):
            rotate90()
            if mat == target:
                return True
        return False