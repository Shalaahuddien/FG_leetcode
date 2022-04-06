class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r = 0, 0
        win = Counter()
        ans = 0
        while r < len(s):
            win[s[r]] += 1
            r += 1
            while len(win) > 2:
                d = s[l]
                win[d] -= 1
                if win[d] == 0:
                    win.pop(d)
                l += 1
            # now local max win of len(win) <= 2
            ans = max(ans, r - l)
        return ans