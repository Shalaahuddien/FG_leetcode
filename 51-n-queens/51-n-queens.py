class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(queens, ddiff, ssum):
            p = len(queens)
            if p == n:
                queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]
                res.append(queens)
                return
            for q in range(n):
                if q in queens or p - q in ddiff or p + q in ssum: continue
                dfs(queens + [q],
                    ddiff + [p - q],
                    ssum + [p + q])
        dfs([], [], [])
        return res