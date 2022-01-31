class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1

        ans = xy // 2 + yx // 2
        mod1, mod2 = xy % 2, yx % 2
        if mod1 == mod2:
            ans += mod1 * 2
            return ans
        else:
            return -1