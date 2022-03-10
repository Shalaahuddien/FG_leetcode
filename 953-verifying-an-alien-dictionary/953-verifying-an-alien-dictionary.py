class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        c2i = {c:i for i,c in enumerate(order)}
        for u,v in zip(words, words[1:]):
            for j in range(len(u)):
                if j >= len(v):
                    return False
                c,d = u[j], v[j]
                if c2i[c] != c2i[d]:
                    if c2i[c] > c2i[d]: return False
                    break
        return True