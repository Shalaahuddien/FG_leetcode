class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x0, y0 = i, j
        res = 0
        for i, j in DIR:
            x, y = x0 + i, y0 + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == "p":
                    res += 1
                    break
                if board[x][y] != ".":
                    break
                x, y = x + i, y + j
        return res