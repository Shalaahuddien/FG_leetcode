class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for x in [tops[0], bottoms[0]]:
            if all(x in d for d in zip(tops, bottoms)):
                return len(tops) - max(tops.count(x), bottoms.count(x))
        return -1
