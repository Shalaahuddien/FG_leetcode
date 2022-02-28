class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = n
        add = 0
        prod = 1
        while x:
            x, r = divmod(x, 10)
            prod *= r
            add += r
        return prod - add
