class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        DEG = Counter()
        for s, d in paths:
            DEG[s] += 1
            DEG[d] += 0
        for c in DEG:
            if DEG[c] == 0:
                return c