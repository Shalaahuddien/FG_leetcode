class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = Counter(nums1)
        res &= Counter(nums2)
        return res.elements()