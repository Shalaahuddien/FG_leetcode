class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def cnt(x):
            seg = 0
            for n in ribbons:
                seg += n // x
            return seg

        l, r = 1, sum(ribbons) // k+1
        while l < r:
            mid = (l + r) // 2
            if cnt(mid) < k:
                r = mid
            else:
                l = mid + 1
        return l - 1