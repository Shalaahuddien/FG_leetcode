class Solution:
    def countHomogenous(self, s: str) -> int:
        l,r,win,ans = 0,0,defaultdict(int),0
        while r < len(s):
            c = s[r]
            r += 1
            win[c] += 1
            while len(win) > 1:
                d = s[l]
                l += 1
                win[d] -=  1
                if win[d]==0:
                    win.pop(d)
            # assert len(win) == 1
            ans += r-l
            ans %= (10**9+7)
        return ans