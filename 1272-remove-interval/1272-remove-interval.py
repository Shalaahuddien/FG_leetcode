class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        ta, tb = toBeRemoved
        for a, b in intervals:
            if (t:= min(b, ta)) > a:
                ans.append([a, t])
            if (t:= max(a, tb)) < b:
                ans.append([t, b])
        return ans