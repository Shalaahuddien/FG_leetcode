class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        # 4//2 = 2: [1,2] => [-1,-2]
        # 5//2 = 2: [1,2] => [-1,-2]+[0]
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2:
            res.append(0)
        return res
