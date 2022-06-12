class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l,r = 0, 0
        win = Counter()
        ans = sm = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            sm += c
            win[c] += 1
            while len(win) < r-l:
                d = nums[l]
                l += 1
                sm -= d
                win[d] -= 1
                if win[d] == 0:
                    win.pop(d)
            # now win is unique
            ans = max(ans, sm)
        return ans