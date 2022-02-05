class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        C = Counter(nums)
        f = lambda x: x * (x - 1) // 2
        return sum(f(v) for v in C.values())