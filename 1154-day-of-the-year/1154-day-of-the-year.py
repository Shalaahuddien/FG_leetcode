class Solution:
    def dayOfYear(self, date: str) -> int:
        yy, mm, dd = map(int, date.split('-'))
        leap = False
        if yy % 4 == 0 and yy % 100:
            leap = True
        elif yy % 400 == 0:
            leap = True
        days = [
            31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]
        pre = [0] * 13
        for i in range(1, 13):
            pre[i] = pre[i - 1] + days[i - 1]
        ans = pre[mm - 1] + dd
        return ans