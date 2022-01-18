class Solution:
    def breakPalindrome(self, pal: str) -> str:
        l = len(pal)
        for i in range(l//2):
            if pal[i] != 'a':
                return pal[:i] + 'a' + pal[i+1:]
        return pal[:-1] + 'b' if l >1 else ''