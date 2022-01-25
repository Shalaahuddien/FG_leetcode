class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i,j,L = 0, len(arr)-1, len(arr)
        while i + 1 < L and arr[i] < arr[i+1]:
            i += 1
        while j-1 >= 0 and arr[j-1] > arr[j]:
            j -= 1
        return 0 < i == j < L-1