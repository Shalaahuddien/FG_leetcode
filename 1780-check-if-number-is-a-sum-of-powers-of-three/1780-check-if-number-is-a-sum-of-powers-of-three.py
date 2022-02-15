class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = n
        while x >= 1:
            x, q = divmod(x, 3)
            if q > 1:
                return False
        return True