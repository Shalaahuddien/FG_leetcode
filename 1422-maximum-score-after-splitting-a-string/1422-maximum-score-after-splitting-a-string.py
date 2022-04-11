class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        mxscore = 0
        l1 = 0
        for i in range(len(s) - 1):
            l1 += s[i] == "1"
            l0 = i + 1 - l1
            r1 = ones - l1
            mxscore = max(mxscore, l0 + r1)
        return mxscore
