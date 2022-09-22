class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()
        res = []
        for l in ss:
            res.append(l[::-1])
        return ' '.join(res)
            