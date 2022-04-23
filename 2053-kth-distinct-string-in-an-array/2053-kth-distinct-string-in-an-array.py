class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for x in arr: 
            if freq[x] == 1: k -= 1
            if k == 0: return x
        return ""