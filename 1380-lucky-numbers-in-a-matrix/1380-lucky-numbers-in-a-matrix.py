class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mnr = []
        res = []
        for r, row in enumerate(matrix):
            mnr.append(row.index(min(row)))
        for c, col in enumerate(zip(*matrix)):
            i = col.index(max(col))
            if mnr[i] == c:
                res.append(matrix[i][c])
        return res