class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fir = bisect_left(nums, target)
        las = bisect_right(nums, target)
        if fir == las:
            return [-1,-1]
        return [fir, las-1]