class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        o = lambda x: ord(x) - ord('a')
        # C = Counter(p)
        C = [0] * 26
        win = [0] * 26
        for c in p:
            C[o(c)] += 1
        res = []
        # win = Counter()
        l, r = 0, 0
        n = len(s)
        while r < n:
            c = s[r]
            r += 1
            win[o(c)] += 1
            while r - l > len(p):
                d = s[l]
                l += 1
                win[o(d)] -= 1
            # now r - l+1 == len(p)
            if win == C:
                res.append(l)
        return res