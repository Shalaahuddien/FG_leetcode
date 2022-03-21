class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: x[0]**2 + x[1]**2
        

        def lomuto(A, L, R):
            pi = randint(L, R)
            A[pi], A[R] = A[R], A[pi]
            pd = dist(A[R])
            l = L - 1
            for i in range(L, R):
                # if less(A[i], p):
                if dist(A[i]) <= pd:
                    l += 1
                    A[l], A[i] = A[i], A[l]
            A[l + 1], A[R] = A[R], A[l + 1]
            return l + 1
        
        def qselect_fxr(l, r):
            """
            Runtime: 992 ms, faster than 10.49% of Python3 online submissions for K Closest Points to Origin.

            T: O(N)
            """

            pi = lomuto(points, l, r)
            if pi == k - 1:
                return points[:k]
            elif pi < k - 1:
                return qselect_fxr(pi + 1, r)
            else:
                return qselect_fxr(l, pi - 1)

        return qselect_fxr(0, len(points) - 1)
