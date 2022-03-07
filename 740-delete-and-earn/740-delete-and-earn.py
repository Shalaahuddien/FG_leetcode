class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        @cache
        def rob(start):
            if start == len(A):
                return 0
            return max(A[start] + (rob(start + 2) if (start + 2) < len(A) else 0), rob(start + 1) if (start + 1) < len(A) else 0)

        A = [0] * (max(nums) + 1)
        for v in nums:
            A[v] += v

        return rob(0)