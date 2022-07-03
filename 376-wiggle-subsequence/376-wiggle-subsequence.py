class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        mxlen, sign = 0, 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1] and sign != -1:  # peak
                sign = -1
                mxlen += 1
            elif nums[i] > nums[i - 1] and sign != 1:  # valley
                sign = 1
                mxlen += 1
        return mxlen + 1