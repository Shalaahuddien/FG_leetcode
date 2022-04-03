class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        k = log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + log(x))

        ans = 0
        for i, x in enumerate(prefix):
            # find max prefix[j] st. prefix[j]-prefix[i] < k
            j = bisect_right(prefix, x + k - 1e-9, i + 1)
            ans += j - i - 1
        return ans