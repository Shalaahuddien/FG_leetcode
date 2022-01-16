class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        if x == res or x == res // 10:
            return True
        return False