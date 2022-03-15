class Solution:
    def trap(self, height: List[int]) -> int:
        stk, res = [], 0
        for i, h in enumerate(height):
            while stk and height[stk[-1]] < h:
                low_i = stk.pop()
                if not stk:
                    break
                W = i - stk[-1] - 1
                H = min(height[stk[-1]], h) - height[low_i]
                res += W * H
            stk.append(i)
        return res
