class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for seat, stu in zip(seats, students):
            res += abs(seat - stu)
        return res