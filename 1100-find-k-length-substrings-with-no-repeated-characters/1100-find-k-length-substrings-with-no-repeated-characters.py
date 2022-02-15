class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        win = defaultdict(int)
        l, r = 0, 0
        ans = 0
        while r < len(s):
            c = s[r]
            r += 1
            win[c] += 1
            while r - l > k:
                d = s[l]
                l += 1
                win[d] -= 1
                if win[d] == 0:
                    del win[d]
            # now [l,r) is k size
            if r - l == k and all(v == 1 for k, v in win.items()):
                ans += 1
        return ans