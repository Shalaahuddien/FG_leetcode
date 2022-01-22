class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, res = [], []
        for n in nums[::-1]:
            i = bisect.bisect_left(arr, n)
            res.append(i)
            arr.insert(i, n)
        return res[::-1]