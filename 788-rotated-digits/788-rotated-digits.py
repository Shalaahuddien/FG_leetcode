class Solution:
    def rotatedDigits(self, n: int) -> int:
        def valid(ns):
            if not any(c in {'3', '4', '7'} for c in ns) and \
                any(c in {'2', '5', '6', '9'} for c in ns):
                return True
            # 0, 1,8
            return False

        ans = 0
        for i in range(1, n + 1):
            if valid(str(i)):
                ans += 1
        return ans