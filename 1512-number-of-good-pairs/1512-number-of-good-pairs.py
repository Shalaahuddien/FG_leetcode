class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        C = Counter(nums)
        f = lambda x: x*(x-1)//2
        ans = 0
        for k,v in C.items():
            ans += f(v)
        return ans