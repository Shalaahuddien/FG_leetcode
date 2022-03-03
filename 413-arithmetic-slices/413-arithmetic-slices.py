class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cnt, tot = 0, 0
        A.append(2e9)
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cnt += 1
            else:
                tot += cnt * (cnt + 1) // 2
                cnt = 0
        return tot