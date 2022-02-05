class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cand = []
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                if cand:
                    return False
                cand.extend([i - 1, i])

        def check(rm):
            A = nums[:rm] + nums[rm + 1:]
            for i in range(1, len(A)):
                if A[i - 1] >= A[i]:
                    return False
            return True

        if not cand:
            return True

        # print(cand)
        return check(cand[0]) or check(cand[1])
