class Solution:
    def reformat(self, s: str) -> str:
        alpha, nums = [], []
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                alpha.append(c)
        if abs(len(alpha) - len(nums)) > 1:
            return ""

        res = []
        if len(alpha) >= len(nums):
            for a, n in zip_longest(alpha, nums, fillvalue=""):
                res.extend([a, n])
        else:
            for n, a in zip_longest(nums, alpha, fillvalue=""):
                res.extend([n, a])
        return "".join(res)