class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            w = r - l
            hl, hr = height[l], height[r]
            h = min(hl, hr)
            ans = max(ans, w * h)
            if hl <= hr:
                l += 1
            else:
                r -= 1
        return ans