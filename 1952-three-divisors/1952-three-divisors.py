class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        cnt = 2
        for d in range(2, isqrt(n) + 1):
            if n % d == 0:
                cnt += 1
                if d * d != n:
                    cnt += 1
                if cnt > 3:
                    break
        return cnt == 3
