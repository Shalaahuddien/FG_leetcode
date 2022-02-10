class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        P = [0]
        D = defaultdict(list)
        D[0].append(-1)
        ans = 0
        for i,n in enumerate(nums):
            P.append(P[-1] + n)
            pre = P[-1] - k
            if pre in D:
                ans += len(D[pre])
            D[P[-1]].append(i)
        return ans