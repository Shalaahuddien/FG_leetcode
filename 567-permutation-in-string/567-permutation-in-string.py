class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        o = lambda c: ord(c) - ord('a')

        win = [0] * 26
        target = [0] * 26
        for c in s1:
            target[o(c)] += 1

        l, r = 0, 0
        if len(s1) > len(s2):
            return False
        while r < len(s2):
            c = s2[r]
            r += 1
            win[o(c)] += 1
            while r - l > len(s1):  #! Don't over-optimize: or s2[l] not in C1 or win[s2[l]] > C1[s2[l]]:
                d = s2[l]
                l += 1
                win[o(d)] -= 1
            # now window size === s1, do the check
            if win == target:
                return True
        return win == target