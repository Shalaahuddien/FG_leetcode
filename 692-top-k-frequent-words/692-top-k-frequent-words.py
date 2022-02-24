class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class Word():

            def __init__(self, freq, word) -> None:
                self.f = freq
                self.w = word

            def __lt__(self, other):
                if self.f == other.f:
                    return self.w > other.w
                return self.f < other.f

        C = Counter(words)
        pq = []
        for w, c in C.items():
            heappush(pq, Word(c, w))
            if len(pq) > k:
                heappop(pq)
        res = [heappop(pq).w for _ in range(k)]
        return res[::-1]