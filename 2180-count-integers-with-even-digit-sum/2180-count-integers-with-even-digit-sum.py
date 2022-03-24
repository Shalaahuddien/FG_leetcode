class Solution:
    def countEven(self, num: int) -> int:
        return sum(1 for n in range(2, num + 1) if sum(map(int, str(n))) % 2 == 0)
