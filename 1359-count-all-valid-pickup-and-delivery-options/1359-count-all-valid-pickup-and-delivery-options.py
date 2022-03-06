class Solution:
    def countOrders(self, n: int) -> int:
        total = 1
        MOD = int(pow(10, 9) + 7)

        for i in range(2, n + 1):
            space = 2 * (i - 1) + 1
            choices = space + space * (space - 1)//2
            total = (total * choices) % MOD
        return total