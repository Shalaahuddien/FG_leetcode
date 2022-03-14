class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for chrs in zip(*strs):
            chrs_set = set(chrs)
            if len(chrs_set) == 1:
                res.append(chrs[0])
            else:
                break
        return "".join(res)