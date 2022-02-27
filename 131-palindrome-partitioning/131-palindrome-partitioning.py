class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def dfs(start):
            if start >= len(s):
                return [[]]
            res = []
            for end in range(start + 1, len(s) + 1):
                pre = s[start:end]
                if pre == pre[::-1]:
                    for lls in dfs(end):
                        res.append([pre] + lls)
            return res

        return dfs(0)