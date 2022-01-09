class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        res = []
        for w in words:
            if len(w) <= 2:
                res.append(w.lower())
            else:
                res.append(w.capitalize())
        return ' '.join(res)