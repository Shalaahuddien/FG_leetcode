"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {e.id: e for e in employees}

        def dfs(id):
            e = mp[id]
            tot = e.importance
            for sub in e.subordinates:
                tot += dfs(sub)
            return tot

        return dfs(id)