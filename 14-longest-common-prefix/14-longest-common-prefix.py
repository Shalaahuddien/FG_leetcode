class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        for cd in zip(first, last):
            if cd[0] != cd[1]:
                return first[:i]
            i += 1
        return first[:i]