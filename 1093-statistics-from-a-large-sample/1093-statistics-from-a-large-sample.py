class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        tot, mode = 0, 0
        median, mn, mx, avg, sm = 0, -1, 0, 0, 0
        for n, f in enumerate(count):
            if f > 0:
                tot += f
                if mn < 0:
                    mn = n
                mx = n
                sm += n * f
                if f > count[mode]:
                    mode = n
        avg = sm / tot

        if tot == 1:
            median = sm
        """
        # common trick
        if x odd, (x+1)//2 === x//2+1
        if x even, (x+1)//2 === x//2
        """
        m1, m2 = 0, 0
        for i in range(255):
            count[i + 1] += count[i]
        m1 = bisect_left(count, tot / 2)
        m2 = bisect_left(count, (tot + 1) / 2)
        median = (m1 + m2) / 2
        # print(m1, m2, median)
        return mn, mx, avg, median, mode