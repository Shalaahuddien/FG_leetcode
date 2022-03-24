class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        C = Counter(nums)
        res = 0
        for b in range(len(target)):
            x, y = target[:b], target[b:]
            if x == y:
                res += C[x] * (C[x] - 1)
            else:
                res += C[x] * C[y]
        return res
