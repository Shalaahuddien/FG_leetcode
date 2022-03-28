class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(p: str) -> bool:
            return (
                any((board[i][0] == p and board[i][1] == p and board[i][2] == p) or (board[0][i] == p and board[1][i] == p and board[2][i] == p) for i in range(3))
                or (board[0][0] == p and board[1][1] == p and board[2][2] == p)
                or (board[0][2] == p and board[1][1] == p and board[2][0] == p)
            )

        oCount = sum(row.count("O") for row in board)
        xCount = sum(row.count("X") for row in board)
        # case 1: xCount must = oCount or oCount+1
        if oCount != xCount and oCount != xCount - 1:
            return False
        # case 2: if X win, must xCount = oCount +1
        if oCount != xCount - 1 and win("X"):
            return False
        # case 3: if O win, must xCount = oCount
        if oCount != xCount and win("O"):
            return False
        return True