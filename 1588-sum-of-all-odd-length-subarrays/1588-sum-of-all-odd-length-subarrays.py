class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        for i,a in enumerate(arr):
            res += ((n-i)*(i+1)+1)//2 * a
        return res