class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        ans = 0
        while True:
            vs = set()
            for i in range(N):
                if ans >= len(strs[i]):
                    return strs[0][:ans]
                v = strs[i][ans]
                vs.add(strs[i][ans])
                if len(vs) >= 2:
                    return strs[0][:ans]
            ans += 1
        return strs[0][:ans]