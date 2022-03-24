class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def calc(x):
            return a * x * x + b * x + c

        n = len(nums)
        idx = 0 if a < 0 else n - 1
        l, r, ans = 0, n - 1, [0] * n
        while l <= r:
            l_val, r_val = calc(nums[l]), calc(nums[r])
            if a >= 0:
                if l_val > r_val:
                    ans[idx] = l_val
                    l += 1
                else:
                    ans[idx] = r_val
                    r -= 1
                idx -= 1
            else:
                if l_val > r_val:
                    ans[idx] = r_val
                    r -= 1
                else:
                    ans[idx] = l_val
                    l += 1
                idx += 1
        return ans