class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_le(x):
            cnt = 0
            c = m - 1
            for r in range(m):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                cnt += c + 1
            return cnt

        m = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if count_le(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l