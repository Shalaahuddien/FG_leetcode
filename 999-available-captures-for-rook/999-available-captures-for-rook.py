class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def capture(i, j):
            cap = 0
            # row
            for r in range(i - 1, -1, -1):
                if board[r][j] == "B":
                    break
                elif board[r][j] == "p":
                    cap += 1
                    break
            for r in range(i + 1, m):
                if board[r][j] == "B":
                    break
                elif board[r][j] == "p":
                    cap += 1
                    break
            for c in range(j - 1, -1, -1):
                if board[i][c] == "B":
                    break
                elif board[i][c] == "p":
                    cap += 1
                    break
            for c in range(j + 1, n):
                if board[i][c] == "B":
                    break
                elif board[i][c] == "p":
                    cap += 1
                    break
            return cap

        m, n = len(board), len(board[0])
        rooks = []
        cnt = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == "R":
                    rooks.append((r, c))

        for i, j in rooks:
            cnt += capture(i, j)
        return cnt