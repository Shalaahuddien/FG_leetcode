class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = 0
        for n in nums:
            if n - 1 in cnt or n + 1 in cnt:
                mx = max(mx, cnt[n - 1] + cnt[n], cnt[n + 1] + cnt[n])
        return mx