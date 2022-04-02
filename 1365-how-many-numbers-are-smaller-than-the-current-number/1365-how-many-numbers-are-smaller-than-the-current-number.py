class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        A = [(n, i) for i, n in enumerate(nums)]
        A.sort()
        res = [0] * len(nums)

        def bileft(x):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if A[mid][0] >= x:
                    r = mid
                else:
                    l = mid + 1
            return l

        for n, i in A:
            j = bileft(n)
            res[i] = j
        return res