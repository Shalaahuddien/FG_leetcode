class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        s = [set(fc) for fc in favoriteCompanies]
        res = []
        for i, s1 in enumerate(s):
            if all(not s1.issubset(s2) for j, s2 in enumerate(s) if i != j):
                res.append(i)
        return res
