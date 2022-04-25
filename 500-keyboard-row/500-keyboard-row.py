class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        one, two, three = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for w in words:
            ws = set(w.lower())
            if ws <= one or ws <= two or ws <= three:
                res.append(w)
        return res