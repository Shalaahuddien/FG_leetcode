class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        C = Counter(nums)
        res = 0
        for x in C:
            if k > 0 and x + k in C:
                res += 1
            elif k == 0 and C[x] > 1:
                res += 1
        return res