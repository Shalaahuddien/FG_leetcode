class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            f, x = nums[i], nums[i + 1]
            res.extend([x] * f)
        return res