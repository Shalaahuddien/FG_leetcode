class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones, zeros = 0, 0
        l, r = 0, 0

        o, z = False, False
        while l < len(s):
            if s[l] == "1":
                o = True
                z = False
            else:
                z = True
                o = False
            cnt = 0
            while r < len(s) and s[r] == s[l]:
                cnt += 1
                r += 1
            # now r out of range or switch 0 <-> 1
            if o:
                ones = max(ones, r - l)
            if z:
                zeros = max(zeros, r - l)
            l = r
        return ones > zeros