class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            """
            http://web.stanford.edu/class/archive/cs/cs106a/cs106a.1212/handouts/mutation.html

            BUG: nums = nums[::-1]
            """
            nums[::] = nums[::-1]
            return
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        nums[k + 1 :] = nums[k + 1 :][::-1]