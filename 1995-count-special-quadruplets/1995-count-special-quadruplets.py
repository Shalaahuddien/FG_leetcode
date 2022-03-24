class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        L = len(nums)
        for i in range(L):
            for j in range(i + 1, L):
                for k in range(j + 1, L):
                    for l in range(k + 1, L):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ans += 1
        return ans
