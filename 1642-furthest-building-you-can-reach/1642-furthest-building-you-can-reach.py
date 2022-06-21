class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        H = heights + [float("inf")]

        def feasible(k):
            L = ladders
            to_climb = [
                y - x for y, x in zip(H[1 : k + 1], H[: k + 1]) if y - x > 0
            ]
            return len(to_climb) <= L or sum(sorted(to_climb)[::-1][L:]) <= bricks

        l, r = 0, len(H) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if feasible(mid):
                l = mid
            else:
                r = mid
        return l