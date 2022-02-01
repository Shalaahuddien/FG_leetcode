class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isleap(year):
            if year % 4 != 0:
                return False
            elif year % 100 != 0:
                return True
            elif year % 400 != 0:
                return False
            return True

        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def f(date):
            y, m, d = map(int, date.split('-'))
            x = 365 * (y - 1971) + sum(map(isleap, range(1971, y)))
            return x + d + sum(days[:m]) + (m > 2 and isleap(y))

        return abs(f(date1) - f(date2))