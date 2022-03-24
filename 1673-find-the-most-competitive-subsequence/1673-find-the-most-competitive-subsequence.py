class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        attempts = len(nums)-k
        stk = []
        for n in nums:
            while attempts and stk and stk[-1] > n:
                stk.pop()
                attempts -= 1
            stk.append(n)
        return stk[:k]