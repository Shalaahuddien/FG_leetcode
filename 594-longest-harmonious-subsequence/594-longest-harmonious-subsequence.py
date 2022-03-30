class Solution:
    def findLHS(self, nums: List[int]) -> int:
        C = Counter()
        mx = 0
        for n in nums:
            C[n] += 1
            if n - 1 in C:
                mx = max(mx, C[n] + C[n - 1])
            if n + 1 in C:
                mx = max(mx, C[n] + C[n + 1])
        return mx