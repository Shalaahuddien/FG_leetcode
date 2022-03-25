class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = Counter(arr).values()
        return len(f) == len(set(f))