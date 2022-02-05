class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row, col = Counter(), Counter()
        for r, c in indices:
            row[r] += 1
            col[c] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2:
                    ans += 1
        return ans
