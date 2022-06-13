class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        below_row = triangle[-1]
        n = len(triangle)
        for r in range(n-2, -1,-1):
            cur_row = []
            for c in range(r+1):
                cur_row.append(triangle[r][c] + min(below_row[c], below_row[c+1]))
            below_row = cur_row
        return below_row[0]