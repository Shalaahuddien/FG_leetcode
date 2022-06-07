class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if m == 0:
        #     nums1[m:] = nums2[:]
        #     return
        # if n == 0:
        #     return
        i,j = m-1,n-1
        for p in range(n+m-1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1