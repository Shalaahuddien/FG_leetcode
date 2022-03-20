class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90():
            n = len(mat)
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1], mat[n - j - 1][i] = mat[n - j - 1][i], mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1]
            # [(i, j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]

        def eq_mat():
            for r in range(len(mat)):
                if mat[r] != target[r]:
                    return False
            return True

        n = len(mat)
        if n == 1:
            return mat[0] == target[0]
        for r in range(4):
            rotate90()
            if eq_mat():
                return True
        return False