class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz = -1
        for i,a in enumerate(A):
            if a != 0:
                nz += 1
                A[i],A[nz]=A[nz],A[i]
        