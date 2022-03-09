class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        REV_PAIRS = ["00", "11", "69", "88", "96"]
        
        @cache
        def dfs(l):
            if l == 0:
                return [""]
            if l == 1:
                return ["0", "1", "8"]
            
            return [xy[0] + n_2 + xy[1] for n_2 in dfs(l - 2) for xy in REV_PAIRS if not (l == n and xy == "00")]

        return dfs(n)