class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotate180 = [[0, 0], [1, 1], [6, 9], [8, 8], [9, 6]]
        self.res = 0

        def dfs(num, numRotated, unit):
            if num != numRotated:
                self.res += 1

            for d, dRotated in rotate180:
                if d == 0 and num == 0: continue  # Skip zero infinity!
                if num * 10 + d > n: break  # Over N already!
                dfs(num * 10 + d, dRotated * unit + numRotated, unit * 10)

        dfs(0, 0, 1)
        return self.res