class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = Counter()
        res = 0
        for b in nums:
            a = k - b
            if seen[a] > 0:
                res += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return res
