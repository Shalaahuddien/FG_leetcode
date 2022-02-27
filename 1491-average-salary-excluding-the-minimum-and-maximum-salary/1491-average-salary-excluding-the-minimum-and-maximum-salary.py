class Solution:
    def average(self, salary: List[int]) -> float:
        mn, mx, tot = 2e9, 0, 0
        for s in salary:
            tot += s
            mn = min(mn, s)
            mx = max(mx, s)
        return (tot - mn - mx) / (len(salary)-2)