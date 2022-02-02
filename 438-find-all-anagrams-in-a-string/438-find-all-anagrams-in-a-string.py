class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        C = Counter(p)
        win = Counter()
        res = []
        l, r = 0, 0
        n = len(s)
        while r < n:
            c = s[r]
            r += 1
            win[c] += 1
            while r - l > len(p):
                d = s[l]
                l += 1
                win[d] -= 1
                if win[d] == 0:
                    del win[d]
            # now r - l+1 == len(p)
            if win == C:
                res.append(l)
        return res