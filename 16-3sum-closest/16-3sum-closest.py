class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        total = sum(nums[:3])
        if total > target:
            return total

        total = sum(nums[-3:])
        if total < target:
            return total
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                total = nums[i] + nums[lo] + nums[hi]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff