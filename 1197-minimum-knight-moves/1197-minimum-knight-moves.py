class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        q1, q2 = set([(0, 0)]), set([(x, y)])
        step = 0
        vis = set([(0, 0), (x, y)])
        DIR = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        while q1:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            q1_nxt = set()
            for i, j in q1:
                if (i, j) in q2:
                    return step
                for dx, dy in DIR:
                    ii, jj = i + dx, j + dy
                    if (ii, jj) in q2:
                        return step + 1
                    if (ii, jj) not in vis and -1 <= ii <= x + 2 and -1 <= jj <= y + 2:
                        vis.add((ii, jj))
                        q1_nxt.add((ii, jj))
            q1 = q1_nxt
            step += 1
        return -1