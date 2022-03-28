class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        tmp = []
        for n, f in cnt.items():
            if n == f:
                tmp.append(n)
        return max(tmp) if tmp else -1