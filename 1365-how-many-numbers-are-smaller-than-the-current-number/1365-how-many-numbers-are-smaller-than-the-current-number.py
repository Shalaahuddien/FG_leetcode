class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        A = [0]*101
        for n in nums:
            A[n] += 1
        pre = 0
        for i,b in enumerate(A):
            if b > 0:
                A[i] = pre
                pre += b
        return [A[n] for n in nums]