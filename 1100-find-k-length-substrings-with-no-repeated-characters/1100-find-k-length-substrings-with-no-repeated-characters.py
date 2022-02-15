class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        freq = [0] * 26
        o = lambda c: ord(c) - ord('a')
        l, r = 0, 0
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            freq[o(c)] += 1
            while freq[o(c)] > 1:
                d = s[l]
                l += 1
                freq[o(d)] -= 1
            # now windows all unique
            if r - l == k:
                res += 1
                d = s[l]
                l += 1
                freq[o(d)] -= 1
        return res