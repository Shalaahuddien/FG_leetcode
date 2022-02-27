class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, s) -> int:
            """[summary]
            Labuladong Ch 2.19
            (i, res) is the state, and we found overlapping subproblems, `say nums[i] = 0`
            memo is map {state -> result}
            """
            # base case
            if i == len(nums):
                if s == 0:
                    return 1
                return 0

            result = dp(i+1, s - nums[i]) + \
                dp(i+1, s+nums[i])

            # XXX: store state and result for CURRENT PROBLEM, not subproblem!!!
            return result

        # driver code
        if not nums:
            return 0
        return dp(0, target)