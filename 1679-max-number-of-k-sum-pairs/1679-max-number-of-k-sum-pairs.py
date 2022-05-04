class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ops = 0
        for n in list(freq.keys()):
            if n * 2 == k:
                ops += freq[n] // 2
                freq.pop(n)
            if k - n in freq:
                ops += min(freq[n], freq[k - n])
                freq.pop(n)
                freq.pop(k - n)
        return ops