class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        P = defaultdict(lambda: [-1, -1])
        F = defaultdict(int)
        mxlen = 0
        for i, n in enumerate(nums):
            if P[n][0] == -1:
                P[n][0] = i
            else:
                P[n][1] = i
            F[n] += 1
            mxlen = max(mxlen, F[n])

        mnlen = len(nums)
        for n, f in F.items():
            if f == mxlen:
                l, r = P[n]
                mnlen = min(mnlen, r - l + 1)
        return max(1, mnlen)