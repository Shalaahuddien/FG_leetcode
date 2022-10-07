from sortedcontainers import SortedDict

# Time Complexity: O(N ^ 2)
# Space Complexity: O(N)
class MyCalendarThree:

    def __init__(self):
        # in line sweeping, we need to ensure the keys are sorted
        # in python, we can use SortedDict which fulfils the above requirement
        # lines[i] = j means we have j overlapping elements at time point i
        self.lines = SortedDict()


    # finding number of overlapping elements at time points -> line sweeping
    def book(self, start: int, end: int) -> int:
        # new event starts here -> increase by 1
        self.lines[start] = self.lines.get(start, 0) + 1
        # the event ends here -> decrease by 1
        # p.s. sometimes you may see `lines.get(end + 1, 0) - 1;`. e.g. 2406. Divide Intervals Into Minimum Number of Groups
        #      you may search `leetcode-the-hard-way` on Discussion to see my solution explanation on that problem
        #      this is because the interval is inclusive, i.e [start, end] 
        #      however, the interval in this problem is [start, end), so we don't need to add 1 here.
        self.lines[end] = self.lines.get(end, 0) - 1
        # here we calculate the prefix sum using `accumulate`
        # and get the maximum overlapping intervals using `max`
        return max(accumulate(self.lines.values()))


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)