class Solution:
    def numberOfSteps(self, num: int) -> int:
        jump = 0
        while num:
            if num % 2 == 1:
                num -= 1
            else:
                num //= 2
            jump += 1
        return jump