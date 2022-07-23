class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, arr = [], []
        # insert the given numbers from right to left, so only numbers after
        # the current one are considered for each number in the array
        for n in nums[::-1]:
            # use binary search to find the insertion point of the current
            # number in the new array, which indicates the count of numbers
            # smaller than the current one so far
            idx = bisect_left(arr, n)
            # the count is what we need for the result
            res.append(idx)
            # insert the current number into the new array
            arr.insert(idx, n)
        # reverse the results since the given numbers are traversed in a
        # reversed order
        print("arr", arr)
        return res[::-1]