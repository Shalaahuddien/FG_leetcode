class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, 0
        for c in s:
            if c == '[':
                l += 1
            else:
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return (l + 1) // 2