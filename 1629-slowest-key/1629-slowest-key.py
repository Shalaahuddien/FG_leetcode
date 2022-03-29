class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        c2d = defaultdict(int)
        prev = 0
        mxdur = 0
        for t, c in zip(releaseTimes, keysPressed):
            dura = t - prev
            mxdur = max(mxdur, dura)
            prev = t
            c2d[c] = max(c2d[c], dura)
        for c in sorted(keysPressed, reverse=True):
            if c2d[c] == mxdur:
                return c
