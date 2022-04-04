class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        fn = lambda x: sum(max(0, xx - x) for xx in inventory)  # balls sold

        # last true binary search
        lo, hi = 0, max(inventory)
        while lo < hi:
            mid = (lo + hi) // 2
            if fn(mid) < orders:  # FFFFTTT
                hi = mid
            else:
                lo = mid + 1

        ans = sum((x + lo + 1) * (x - lo) // 2 for x in inventory if x > lo)
        return (ans - (fn(lo) - orders) * (lo)) % 1_000_000_007