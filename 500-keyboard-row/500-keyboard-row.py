class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        one, two, three = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for w in words:
            for s in (one, two, three):
                if w[0].lower() in s:
                    break
            if all(c.lower() in s for c in w[1:]):
                res.append(w)
        return res