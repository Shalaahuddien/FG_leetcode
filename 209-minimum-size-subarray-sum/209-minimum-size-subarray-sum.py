class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ans = 1e9
        # presum[0] means sum of first 0 elements, presum[k] means sum of first k elements
        presum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            to_find = target + presum[i - 1]  # to_find - presum[i] = target
            bound = bisect_left(presum, to_find)
            if bound != len(presum):
                ans = min(ans, (bound - (i - 1)))
        return ans if ans != 1e9 else 0