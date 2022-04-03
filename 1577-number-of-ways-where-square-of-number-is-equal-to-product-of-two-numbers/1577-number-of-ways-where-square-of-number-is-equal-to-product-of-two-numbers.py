class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        F1, F2 = Counter([n**2 for n in nums1]), Counter([n**2 for n in nums2])

        def aggregateType(nums, F):
            total = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    target = nums[i] * nums[j]
                    total += F[target]
            return total

        return aggregateType(nums1, F2) + aggregateType(nums2, F1)