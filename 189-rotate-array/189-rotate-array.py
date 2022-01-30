class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l,r = l+1,r-1
        L = len(nums)
        k = k%L
        rev(0, L-k-1)
        rev(L-k,L-1)
        rev(0,L-1)
        