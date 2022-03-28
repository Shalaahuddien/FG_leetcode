class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            if l == r:
                return nums[l] == target
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l] == target
