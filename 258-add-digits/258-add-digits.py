class Solution:
    def addDigits(self, num: int) -> int:
        x = num
        while x >= 10:
            x = sum(map(int, str(x)))
        return x
