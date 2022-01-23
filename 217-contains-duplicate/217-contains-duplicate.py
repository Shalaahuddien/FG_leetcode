class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pigeons = len(nums)
        holes = len(set(nums))
        return pigeons > holes