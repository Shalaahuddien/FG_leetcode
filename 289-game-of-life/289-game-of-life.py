class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def cntNei(i, j):
            return sum(1 for x in (i - 1, i, i + 1) for y in (j - 1, j, j + 1) if 0 <= x < m and 0 <= y < n and board[x][y] & 1)

        # count neighbors
        for i in range(m):
            for j in range(n):
                cnt = cntNei(i, j)
                cnt -= board[i][j]  # because we included the cell in the neighbors count
                print(i, j, cnt)
                if cnt == 3 or (cnt == 2 and board[i][j] == 1):  # live conditions
                    board[i][j] |= 2  # equivalent to board[i][j] |= 1<<1 --- set the 2nd bit which is the next set

        # convert back
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        print(board)