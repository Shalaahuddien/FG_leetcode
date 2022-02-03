class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        l, r = 2, num // 2
        while l < r:
            mid = (l + r) // 2
            if mid**2 >= num:
                r = mid
            else:
                l = mid + 1
        # print(l)
        return l**2 == num