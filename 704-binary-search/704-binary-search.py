class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1
        if nums[l] == target:
            return l
        return -1