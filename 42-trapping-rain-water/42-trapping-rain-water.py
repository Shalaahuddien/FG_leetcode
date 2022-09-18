class Solution:
    def trap(self, height: List[int]) -> int:
        i, j, ans, mx, mi = 0, len(height) - 1, 0, 0, 0
        # two pointers 
        # pointer i from the left
        # pointer j from the right
        while i <= j:
            # take the min height
            mi = min(height[i], height[j])
            # find the max min height
            mx = max(mx, mi)
            # the units of water being tapped is the diffence between max height and min height
            ans += mx - mi
            # move the pointer i if height[i] is smaller
            if height[i] < height[j]: i += 1
            # else move pointer j
            else: j -= 1
        return ans