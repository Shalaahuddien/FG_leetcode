class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(s)
        for i, c in zip(indices, s):
            res[i] = c
        return "".join(res)
