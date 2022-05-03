class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        while True:
            l = len(students)
            for _ in range(l):
                if students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.popleft()
                else:
                    students.append(students.popleft())
            if l == len(students):
                break
        return len(students)