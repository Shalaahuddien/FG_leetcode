class Solution:
    def countArrangement(self, n: int) -> int:
        memo = defaultdict(int)

        def dfs(bm, pl):
            """
            bm is binary mask for visited numbers.
            pl is current place we want to fill. 
            XXX: Idea is to start from the end, and fill places in opposite direction, because for big numbers we potentially have less candidates.
            """
            if (bm, pl) in memo:
                # print((bm, pl))
                return memo[(bm, pl)]
            if pl == 0:
                return 1
            S = 0
            for i in range(n):
                if not bm & (1 << i) \
                    and ((i + 1) % pl == 0 or pl % (i + 1) == 0):
                    S += dfs(bm ^ (1 << i), pl - 1)
            memo[(bm, pl)] = S
            return S

        return dfs(0, n)