class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)

        def ok(k):
            # the idea is to use binary search to find the length `k`
            # then we check if there is any nums1[i : i + k] == nums2[i : i + k]
            s = set(tuple(nums1[i : i + k]) for i in range(N - k + 1))
            return any(tuple(nums2[i : i + k]) in s for i in range(M - k + 1))

        # init possible boundary
        l, r = 0, min(N, M)
        while l < r:
            # get the middle one
            # for even number of elements, take the upper one
            m = (l + r + 1) // 2
            if ok(m):
                # include m
                l = m
            else:
                # exclude m
                r = m - 1
        return l