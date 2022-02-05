class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        oddr,oddc = [False]*m, [False]*n
        for r,c in indices:
            oddr[r] ^= True
            oddc[c] ^= True
        orc = sum(oddr)
        occ = sum(oddc)
        return orc * (n-occ) + occ*(m-orc)
        