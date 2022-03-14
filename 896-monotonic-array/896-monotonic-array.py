class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sign = lambda x: bool(x > 0) - bool(x < 0)
        sn = sign(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            if sn == 0:
                if not nums[i - 1] == nums[i]:
                    return False
            elif sn == 1:
                if not nums[i - 1] <= nums[i]:
                    return False
            else:
                if not nums[i - 1] >= nums[i]:
                    return False
        return True