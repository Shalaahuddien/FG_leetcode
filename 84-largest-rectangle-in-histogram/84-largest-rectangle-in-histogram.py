class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []
        for i, hi in enumerate(heights + [0]):
            while stk and heights[stk[-1]] > hi:
                h = heights[stk.pop()]
                if stk:
                    w = i - stk[-1] - 1
                else:
                    w = i
                ans = max(ans, w * h)
            # now stk mono-incr
            stk.append(i)
        return ans