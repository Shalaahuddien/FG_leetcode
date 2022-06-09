class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        l = r = 0
        win = mx_one = 0
        while r < len(data):
            win += data[r]
            r += 1
            while r-l > ones:
                win -= data[l]
                l += 1
            # now r-l+1= ones
            mx_one = max(mx_one, win)
        return ones - mx_one