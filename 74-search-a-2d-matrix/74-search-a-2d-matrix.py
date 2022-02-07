class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l < r:
            mid = (l + r) // 2
            x, y = divmod(mid, n)
            v = matrix[x][y]
            if v >= target:
                r = mid
            else:
                l = mid + 1

        x, y = divmod(l, n)
        return matrix[x][y] == target