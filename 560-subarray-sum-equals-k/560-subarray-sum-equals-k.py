class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        P = 0
        D = defaultdict(int)
        D[0] += 1
        ans = 0
        for i,n in enumerate(nums):
            P += n
            pre = P - k
            if pre in D:
                ans += D[pre]
            D[P] += 1
        return ans