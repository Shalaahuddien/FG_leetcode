class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        C = Counter(s)
        return len(set(C.values())) == 1
    