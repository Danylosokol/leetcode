from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_q = deque(students)
        sandwiches_q = deque(sandwiches)

        counter = 0

        while len(students_q) > counter:
            student = students_q.popleft()
            if student == sandwiches_q[0]:
                sandwiches_q.popleft()
                counter = 0
            else:
                students_q.append(student)
                counter += 1
        return len(students_q)
            


        