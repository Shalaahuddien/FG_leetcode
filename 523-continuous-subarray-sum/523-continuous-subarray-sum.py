class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        pre = 0
        pre_r = {0: -1}
        for i in range(N):
            pre = pre + nums[i]
            remainder = pre % k
            if i - pre_r.setdefault(remainder, i) >= 2:
                return True
        return False