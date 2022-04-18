class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        nums = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j].isdigit():
                    nums[i][j] = board[i][j]
                if board[i][j] == "M":
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            ni, nj = i + dx, j + dy
                            if not (0 <= ni < m and 0 <= nj < n):
                                continue
                            if board[ni][nj] == "E":
                                nums[ni][nj] = str(int(nums[ni][nj]) + 1)
        vis = set()

        def dfs(i, j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return
            if nums[i][j] != 0:
                board[i][j] = nums[i][j]
                return
            board[i][j] = "B"
            vis.add((i, j))
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    ni, nj = i + dx, j + dy
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if (ni, nj) in vis:
                        continue
                    if board[ni][nj] == "M":
                        continue
                    dfs(ni, nj)

        dfs(click[0], click[1])
        return board