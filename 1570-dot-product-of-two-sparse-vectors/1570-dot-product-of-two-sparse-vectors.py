class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = []
        for i,x in enumerate(nums):
            if x != 0:
                self.d.append((i,x))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i,j=0,0
        while i < len(self.d) and j < len(vec.d):
            if self.d[i][0] == vec.d[j][0]:
                res += self.d[i][1] * vec.d[j][1]
                i,j = i+1,j+1
            elif self.d[i][0] < vec.d[j][0]:
                i += 1
            else:
                j+=1
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)