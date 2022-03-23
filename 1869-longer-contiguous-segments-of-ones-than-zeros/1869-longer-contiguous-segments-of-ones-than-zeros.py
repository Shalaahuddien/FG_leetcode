class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mx_one, mx_zero, cur_one, cur_zero = 0, 0, 0, 0
        for c in s:
            if c == "1":
                cur_zero = 0
                cur_one += 1
            else:
                cur_zero += 1
                cur_one = 0

            mx_one = max(mx_one, cur_one)
            mx_zero = max(mx_zero, cur_zero)
        return mx_one > mx_zero