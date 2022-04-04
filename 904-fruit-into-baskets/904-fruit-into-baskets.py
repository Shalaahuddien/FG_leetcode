class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        used = Counter()
        mx = 0
        while r < len(fruits):
            c = fruits[r]
            r += 1
            used[c] += 1
            while len(used) > 2:
                d = fruits[l]
                l += 1
                if d in used:
                    used[d] -= 1
                    if used[d] == 0:
                        used.pop(d)
            # max window with <= 2 used
            mx = max(mx, r - l)
        return mx