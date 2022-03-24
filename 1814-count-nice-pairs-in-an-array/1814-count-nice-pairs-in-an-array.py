class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freq = Counter()
        res = 0
        for a in nums:
            b = int(str(a)[::-1])
            res += freq[a - b]
            freq[a - b] += 1
        return res % (10**9 + 7)