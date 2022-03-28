class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {p[0]: p for p in pieces}
        res = []
        for n in arr:
            res += mp.get(n, [])
        return res == arr
