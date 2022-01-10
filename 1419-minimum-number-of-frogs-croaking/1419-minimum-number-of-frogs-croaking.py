class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        watermark = c = r = o = a = k = 0
        for x in croakOfFrogs:
            if x == 'c':
                c += 1
                watermark = max(watermark, c - k)
            elif x == 'r':
                r += 1
            elif x == 'o':
                o += 1
            elif x == 'a':
                a += 1
            else:
                k += 1
            if not c >= r >= o >= a >= k:
                return -1
        return watermark if c == k else -1