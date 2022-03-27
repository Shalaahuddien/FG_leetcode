class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freqs = Counter(deck).values()
        return gcd(*freqs) >= 2