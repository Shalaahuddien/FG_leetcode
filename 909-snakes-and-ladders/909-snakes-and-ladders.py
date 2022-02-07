class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        start = (1, 0)
        vis = set([1])
        q = deque([start])

        def toRC(pos):
            r, c = divmod(pos - 1, n)
            return ~r, c if r % 2 == 0 else ~c

        while q:
            pos, stp = q.popleft()
            if pos == n * n:
                return stp
            for pp in range(pos + 1, pos + 7):
                if pp > n * n:
                    continue
                r, c = toRC(pp)
                nxt = board[r][c]
                if nxt > 0:
                    pp = nxt
                if pp not in vis:
                    q.append((pp, stp + 1))
                    vis.add(pp)
        return -1