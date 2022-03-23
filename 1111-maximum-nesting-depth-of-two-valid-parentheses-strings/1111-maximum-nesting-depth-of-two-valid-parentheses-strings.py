class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        mxop = 0
        bal = 0
        for c in seq:
            if c == "(":
                bal += 1
                mxop = max(mxop, bal)
            else:
                bal -= 1
        thrd = (mxop + 1) // 2
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == "(":
                bal += 1
                if bal > thrd:
                    res[i] = 1
            else:
                if bal > thrd:
                    res[i] = 1
                bal -= 1
        return res
