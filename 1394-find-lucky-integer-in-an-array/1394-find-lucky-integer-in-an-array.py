class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans_n, ans_f = None, 0
        for n, f in cnt.items():
            if n == f and ans_f <= f:
                ans_f = f
                ans_n = n
        return ans_n if ans_n else -1