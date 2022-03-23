class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, src, tar in sorted(zip(indices, sources, targets), reverse=True):
            s = s[:i] + tar + s[i + len(src) :] if s[i : i + len(src)] == src else s
        return s