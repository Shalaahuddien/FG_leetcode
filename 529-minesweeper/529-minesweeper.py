class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def reveal(i, j):
            # board is: M, E, B, 1~8, X
            if not valid(i, j) or board[i][j] != "E":
                return
            # count (i,j)'s adjacent mines
            mines = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    ni, nj = i + dx, j + dy
                    if valid(ni, nj) and board[ni][nj] == "M":
                        mines += 1
            if mines:
                board[i][j] = str(mines)
                return
            else:
                board[i][j] = "B"
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        reveal(i + dx, j + dy)

        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            reveal(x, y)
        return board
