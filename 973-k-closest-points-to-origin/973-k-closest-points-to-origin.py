class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: x[0]**2 + x[1]**2
        def lomuto(A, l, r):
            d = randint(l, r)  # random int in [l...r]
            A[d], A[r] = A[r], A[d]
            pdist = dist(A[r])
            i = l - 1
            for j in range(l, r):
                if dist(A[j]) <= pdist:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            A[i + 1], A[r] = A[r], A[i + 1]
            return i + 1

        l, r, p = 0, len(points) - 1, 0
        while l < r:
            p = lomuto(points, l, r)
            if p == k-1:
                break
            elif p > k-1:
                r = p-1
            else:
                l = p + 1
        return points[: k]