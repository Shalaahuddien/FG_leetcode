class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def cnt(i, j):
            ones = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x, y = i + dx, j + dy
                    if (x, y) == (i, j):
                        continue
                    if 0 <= x < m and 0 <= y < n:
                        ones += copy_board[x][y]
            return ones

        m, n = len(board), len(board[0])
        copy_board = [[board[r][c] for c in range(n)] for r in range(m)]
        for i in range(m):
            for j in range(n):
                ones = cnt(i, j)
                # print(i, j, ones)
                if copy_board[i][j] == 1:
                    if ones < 2:
                        board[i][j] = 0
                    elif 2 <= ones <= 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if ones == 3:
                        board[i][j] = 1
        return board