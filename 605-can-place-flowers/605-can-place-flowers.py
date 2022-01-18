class Solution:
    def canPlaceFlowers(self, F: List[int], n: int) -> bool:
        cnt = 0
        F = [1, 0] + F + [0, 1]
        ones = []
        for i, c in enumerate(F):
            if c == 1:
                ones.append(i)
        for p, c in zip(ones, ones[1:]):
            cnt += max(0, (c - p - 2)) // 2
        return cnt >= n
