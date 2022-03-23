class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        lwi = [(w, i) for i, w in enumerate(words)]
        lwi.sort(key=lambda x: (len(x[0]), x[1]))
        res = [w.lower() for w, i in lwi]
        return " ".join(res).capitalize()
