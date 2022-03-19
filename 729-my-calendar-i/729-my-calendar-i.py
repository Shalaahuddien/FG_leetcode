from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        def __overlap(e1, e2) -> bool:
            if e1[1] <= e2[0] or e1[0] >= e2[1]:
                return False
            return True

        event = (start, end)
        i = self.calendar.bisect_left(event)

        n = len(self.calendar)
        if (i < n and __overlap(event, self.calendar[i])) or (i > 0 and __overlap(event, self.calendar[i - 1])):
            return False
        self.calendar.add(event)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)