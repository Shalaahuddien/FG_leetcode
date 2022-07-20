class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(word):
            curr = 0
            for c in word:
                ind = bisect_left(places[c], curr)
                if ind >= len(places[c]):
                    return False
                curr = places[c][ind] + 1

            return True

        places = defaultdict(list)
        for i, c in enumerate(s):
            places[c].append(i)

        return sum(isSubseq(word) for word in words)