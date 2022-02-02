class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        for a in words:
            res &= Counter(a)
        return res.elements()