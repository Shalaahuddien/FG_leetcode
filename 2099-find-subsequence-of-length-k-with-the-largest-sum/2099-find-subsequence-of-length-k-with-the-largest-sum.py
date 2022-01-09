class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = sorted(list((x, i) for i, x in enumerate(nums)))
        n = n[-k:]
        n = sorted(list((i, x) for x, i in n))
        n = list(x for _, x in n)
        return n