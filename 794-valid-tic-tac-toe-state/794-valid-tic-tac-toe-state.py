class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        allsum = 0
        win = 0
        row = [0] * 3
        col = [0] * 3
        diag = antidiag = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                play = 0
                if board[r][c] == "X":
                    play = 1
                elif board[r][c] == "O":
                    play = -1
                row[r] += play
                col[c] += play
                if r == c:
                    diag += play
                if r + c == len(board)-1:
                    antidiag += play
                allsum += play
        if not 0 <= allsum <= 1:
            return False

        states = [*row, *col, diag, antidiag]
        xwin = any(s == 3 for s in states)
        owin = any(s == -3 for s in states)
        if xwin == owin == True:
            return False
        if xwin:
            if allsum != 1:
                return False
        if owin:
            if allsum != 0:
                return False
        return True