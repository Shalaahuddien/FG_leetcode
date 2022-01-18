class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        L = len(heights)
        ans = []
        mx_height = -1
        for i in reversed(range(L)):
            if mx_height < heights[i]:
                ans.append(i)
                mx_height = heights[i]
        ans.reverse()
        return ans