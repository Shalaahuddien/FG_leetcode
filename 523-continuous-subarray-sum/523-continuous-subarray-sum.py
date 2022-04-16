class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        pre = [0] * (N + 1)
        pre_r = {0: -1}
        for i in range(N):
            pre[i + 1] = pre[i] + nums[i]
            remainder = pre[i + 1] % k
            if i - pre_r.setdefault(remainder, i) >= 2:
                return True
        return False