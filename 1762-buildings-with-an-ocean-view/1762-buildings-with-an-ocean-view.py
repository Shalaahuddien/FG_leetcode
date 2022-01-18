class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l = len(heights)
        stk = []
        ng = [-1] * l
        ans = []
        for i in range(l - 1, -1, -1):
            while stk and heights[stk[-1]] < heights[i]:
                stk.pop()
            ng[i] = stk[-1] if stk else -1
            if ng[i] == -1:
                ans.append(i)
            stk.append(i)
        return ans[::-1]