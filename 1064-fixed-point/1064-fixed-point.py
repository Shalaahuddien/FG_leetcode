class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l,r = 0, len(arr)-1
        while l < r:
            mid = (l+r)//2
            if arr[mid] >= mid:
                r = mid
            else:
                l = mid+1
        if arr[l] == l:
            return l
        return -1