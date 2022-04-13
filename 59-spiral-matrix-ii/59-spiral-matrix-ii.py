class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        st = 0  # 0: right, 1: down, 2: left: 3: up
        M = [[0] * n for _ in range(n)]
        L, R, U, B = 0, n - 1, 0, n - 1
        r, c = 0, 0
        for v in range(1, n * n + 1):
            # r, c = divmod(co, n)
            M[r][c] = v
            if st == 0:
                c += 1
                if c == R:
                    st = (st + 1) % 4
                    U += 1
            elif st == 1:
                r += 1
                if r == B:
                    st = (st + 1) % 4
                    R -= 1
            elif st == 2:
                c -= 1
                if c == L:
                    st = (st + 1) % 4
                    B -= 1
            else:
                r -= 1
                if r == U:
                    st = (st + 1) % 4
                    L += 1

        return M