class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        bad = set(forbidden)
        footprint = set()
        upper = max(forbidden + [x]) + a + b
        res = [1e6]

        def dfs(p, cnt, prev):
            """
            prev: last direction. True=backed, False=not backed
            """
            if not 0 <= p <= upper:
                return
            if p in bad:
                return
            if (p, prev) in footprint:
                return
            if p == x:
                res[0] = min(res[0], cnt)
                return

            footprint.add((p, prev))

            dfs(p + a, cnt + 1, False)
            if not prev:
                dfs(p - b, cnt + 1, True)

        dfs(0, 0, True)
        dfs(0, 0, False)
        return -1 if res[0] == 1e6 else res[0]