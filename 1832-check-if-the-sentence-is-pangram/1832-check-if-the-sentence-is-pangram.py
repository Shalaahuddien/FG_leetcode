class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for w in sentence.split():
            for c in w:
                seen.add(c)
        return len(seen) == 26
