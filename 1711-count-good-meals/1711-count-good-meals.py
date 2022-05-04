class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = Counter()
        res = 0
        for x in deliciousness:
            for k in range(22):
                res += freq[2**k - x]
            freq[x] += 1
        return res % (10**9 + 7)