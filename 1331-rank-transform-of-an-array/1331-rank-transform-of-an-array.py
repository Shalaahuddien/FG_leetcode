class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {n:r+1 for r,n in enumerate(sorted(set(arr)))}
        return map(ranks.get, arr)