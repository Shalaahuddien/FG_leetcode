class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l = len(heights)
        stk = []
        ans = []
        for i in range(l - 1, -1, -1):
            while stk and heights[stk[-1]] < heights[i]:
                stk.pop()
            if not stk:
                ans.append(i)
            stk.append(i)
        ans.reverse()
        return ans