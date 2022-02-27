class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        @cache
        def memo(nums):
            """
            https://leetcode.com/problems/permutations/discuss/1722569/Python3-solution-with-memoization
            XXX: All backtrack/DFS can become @cache, just make it return res!
            """
            if not nums:
                return [[]]
            res = []
            for i in range(len(nums)):
                subprob = memo(tuple(nums[:i] + nums[i + 1:]))
                for t in subprob:
                    res.append([nums[i]] + t)
            return res

        return memo(tuple(nums))
