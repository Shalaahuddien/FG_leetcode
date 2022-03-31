class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mnr = {min(row) for row in matrix}
        mxc = {max(col) for col in zip(*matrix)}
        return list(mnr & mxc)
