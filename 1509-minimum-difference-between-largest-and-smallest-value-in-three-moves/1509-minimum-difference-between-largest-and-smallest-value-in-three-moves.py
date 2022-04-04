class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        # first 3 becomes 4
        fir3 = nums[-1] - nums[3]
        # last 3 becomes -4
        las3 = nums[-4] - nums[0]
        # fir1 last2
        fir1las2 = nums[-3] - nums[1]
        # fir2 last1
        fir2las1 = nums[-2] - nums[2]

        return min(fir3, las3, fir1las2, fir2las1)