class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = longest_subarr = 0
        indices = {}

        for i, num in enumerate(nums):
            presum += num

            # Check if all of the numbers seen so far sum to k.
            if presum == k:
                longest_subarr = i + 1

            # If any subarray seen so far sums to k, then
            # update the length of the longest_subarray.
            elif presum - k in indices:
                longest_subarr = max(longest_subarr, i - indices[presum - k])

            # Only add the current prefix_sum index pair to the
            # map if the prefix_sum is not already in the map.
            if presum not in indices:
                indices[presum] = i

        return longest_subarr