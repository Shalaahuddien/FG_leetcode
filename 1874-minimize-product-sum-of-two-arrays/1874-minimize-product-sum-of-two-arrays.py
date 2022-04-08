class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=True)
        nums2.sort()
        sm = 0
        for i in range(len(nums1)):
            sm += nums1[i] * nums2[i]
        return sm
