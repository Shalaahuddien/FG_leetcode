class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c2o = {c: o for o, c in enumerate(order)}
        freq = Counter(s)

        res = []
        for c in c2o.keys():
            if c in freq:
                res.extend([c] * freq[c])
        for ow in freq.keys() - c2o.keys():
            res.extend([ow] * freq[ow])
        return "".join(res)