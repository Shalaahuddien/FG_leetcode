class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        C = Counter(words)
        # top k => min k
        pq = []
        for w,f in C.items():
            heappush(pq, (-f,w))
        return [heappop(pq)[1] for _ in range(k)]