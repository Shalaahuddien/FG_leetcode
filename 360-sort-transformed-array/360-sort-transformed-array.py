class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def calc(x):
            return a * x**2 + b * x + c

        def shuxue():
            if a == 0:
                return nums
            turn = -b / 2 / a

            idx = bisect_left(nums, turn)
            if idx <= 0 or idx >= len(nums):
                return nums
            l, r = idx - 1, idx
            res = []
            while l >= 0 and r < len(nums):
                if abs(nums[l] - turn) < abs(nums[r] - turn):
                    res.append(nums[l])
                    l -= 1
                else:
                    res.append(nums[r])
                    r += 1
            # print(l, r)
            res.extend(nums[: l + 1][::-1] if l >= 0 else nums[r:])
            return res

        ans = list(map(calc, shuxue()))
        if ans[0] > ans[-1]:
            return ans[::-1]
        return ans