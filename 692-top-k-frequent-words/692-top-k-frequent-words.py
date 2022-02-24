class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        F = Counter(words)
        tmp = nsmallest(k, F.items(), key=lambda x: (-x[1], x[0]))
        return [w for w, f in tmp]