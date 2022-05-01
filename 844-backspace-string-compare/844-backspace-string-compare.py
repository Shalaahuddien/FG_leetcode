class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        backs = backt = 0
        while i >= 0 or j >= 0:
            # i stops at non-deleted character in S or -1
            while i >= 0:
                if s[i] == "#":
                    backs += 1
                    i -= 1
                elif s[i] != "#" and backs > 0:
                    backs -= 1
                    i -= 1
                else:
                    break
            # hi stops at non-deleted character in T or -1
            while j >= 0:
                if t[j] == "#":
                    backt += 1
                    j -= 1
                elif t[j] != "#" and backt > 0:
                    backt -= 1
                    j -= 1
                else:
                    break
            # XXX
            if (i < 0 and j >= 0) or (j < 0 and i >= 0):
                # eg. S = 'a#', T = 'a'
                return False
            if (i >= 0 and j >= 0) and s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True