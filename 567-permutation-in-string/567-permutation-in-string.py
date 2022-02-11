class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win = Counter()
        C1 = Counter(s1)
        l, r = 0, 0
        if len(s1) > len(s2):
            return False
        while r < len(s2):
            c = s2[r]
            r += 1
            win[c] += 1
            while r - l > len(s1):  # or s2[l] not in C1 or win[s2[l]] > C1[s2[l]]:
                d = s2[l]
                l += 1
                win[d] -= 1
                if win[d] == 0:
                    del win[d]
            if win == C1:
                return True
        return win == C1