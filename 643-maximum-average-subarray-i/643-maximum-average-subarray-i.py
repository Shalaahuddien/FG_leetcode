class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = now = sum(nums[:k])
        for i in range(k, len(nums)):
            now += nums[i] - nums[i - k]
            best = max(best, now)
        return best / k

