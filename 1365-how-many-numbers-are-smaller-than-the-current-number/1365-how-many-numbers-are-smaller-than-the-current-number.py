class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        A = {}
        for i,n in enumerate(sorted(nums)):
            A.setdefault(n,i)
        return [A[n] for n in nums]