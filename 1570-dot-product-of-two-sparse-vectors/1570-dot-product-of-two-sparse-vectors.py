class SparseVector:
    def __init__(self, nums: List[int]):
        self.nz = set()
        self.nums = nums
        for i, v in enumerate(nums):
            if v:
                self.nz.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nz = self.nz.intersection(vec.nz)
        ans = 0
        for i in nz:
            ans += self.nums[i] * vec.nums[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)